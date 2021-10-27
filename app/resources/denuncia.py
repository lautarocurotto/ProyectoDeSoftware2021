from datetime import datetime
from flask import redirect, render_template, request, url_for, session, abort, flash
from werkzeug.wrappers import response
from app.models.denuncia import Denuncia
from app.helpers.paginator import Paginator
from app.models.configuracion import Configuracion
from app.helpers.auth import authenticated, check_permission
from email_validator import validate_email, EmailNotValidError

from app.db import db

status_names = ["UNCONFIRMED", "IN_PROGRESS", "RESOLVED", "CLOSED"]

def index():

    if not authenticated(session) or not check_permission(session["id"], "denuncia_index"):
        abort(401)

    return render_template("denuncia/denuncias.html", paginator=Paginator(Denuncia.get_all(request.args), Configuracion.getConfigs().maxElementos, request.args.get("page", 0)))

def show(id):
    if not authenticated(session) or not check_permission(session["id"], "denuncia_update"):
        abort(401)

    return render_template("denuncia/show.html", denuncia=Denuncia.query.get_or_404(id))

def set_status():

    if not authenticated(session) or not check_permission(session["id"], "denuncia_update") and (request.form["status"] == '' and request.form["id"] == ''):
        abort(401)

    if not request.form["status"] in status_names:
        abort(500)

    Denuncia.query.get_or_404(request.form["id"]).status = request.form["status"]

    # En caso de que se re-abra la denuncia, borrar la fecha de clsed_at
    if(request.form["status"] == "CLOSED"):
        Denuncia.query.get_or_404(request.form["id"]).closed_at = datetime.now()
    else:
        Denuncia.query.get_or_404(request.form["id"]).closed_at = ""
    

    try:
        db.session.commit()
        flash("Estado de denuncia actualizado")
    except:
        print("Error @ denuncia#set_status()")
        flash("Error")
    
    return redirect(url_for('denuncia_show', id = request.form["id"]))

def update_seguimiento():
    if not authenticated(session) or not check_permission(session["id"], "denuncia_update") and (request.form["seguimientos"] == '' and request.form["id"] == ''):
        abort(401)

    if Denuncia.query.get_or_404(request.form["id"]).status == "CLOSED":
        flash("Esta denuncia está cerrada. Debe reabrirla para poder gestionarla.")
        return redirect(url_for("denuncia_show", id = request.form["id"]))

    Denuncia.query.get_or_404(request.form["id"]).seguimiento = request.form["seguimiento"]

    try:
        db.session.commit()
        flash("Seguimiento de denuncia actualizado")
    except:
        print("Error @ denuncia#update_seguimiento()")
        flash("Error")

    return redirect(url_for('denuncia_show', id = request.form["id"]))

def new_denuncia():
    postdata = request.get_json()

    try:
        validate_email(postdata["email_denunciante"])
    except EmailNotValidError:
        return "Email inválido"

    try:
        int(postdata["categoria_id"])
    except:
        return "ID de categoría inválido"

    if postdata["coordenadas"] == '':
        return return_missing_field_error("unas coordenadas")

    if postdata["apellido_denunciante"] == '':
        return return_missing_field_error("su apellido")

    if postdata["nombre_denunciante"] == '':
        return return_missing_field_error("su nombre")

    if postdata["telcel_denunciante"] == '':
        return return_missing_field_error("su número telefónico")

    if postdata["titulo"] == '':
        return return_missing_field_error("un título")

    if postdata["descripcion"] == '':
        return return_missing_field_error("una descripcion")

    db.session.add(
        Denuncia(
            category_id = postdata["categoria_id"],
            coordenates = postdata["coordenadas"],
            denunciante_name = postdata["nombre_denunciante"],
            denunciante_last_name = postdata["apellido_denunciante"],
            denunciante_phone = postdata["telcel_denunciante"],
            denunciante_email = postdata["email_denunciante"],
            title = postdata["titulo"],
            description = postdata["descripcion"]
        ))

    try:
        db.session.commit()
    except Exception as e:
        return (str(e))
        
    return response.Response(status=201)

def return_missing_field_error(fieldname):
    return "Debe introducir " + fieldname
