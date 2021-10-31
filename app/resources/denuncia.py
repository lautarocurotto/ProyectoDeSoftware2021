from datetime import datetime
from flask import redirect, render_template, request, url_for, session, abort, flash
from werkzeug.wrappers import response
from app.models.denuncia import Denuncia
from app.helpers.paginator import Paginator
from app.models.configuracion import Configuracion
from app.helpers.auth import authenticated, check_permission
from email_validator import validate_email, EmailNotValidError
from app.models.seguimiento import Seguimiento
from app.models.categoria import Categoria

from app.db import db

status_names = ["UNCONFIRMED", "IN_PROGRESS", "RESOLVED", "CLOSED"]

def index():
    """Obtener y mostrar todas las denuncias"""

    if not authenticated(session) or not check_permission(session["id"], "denuncia_index"):
        abort(401)

    return render_template("denuncia/denuncias.html", paginator=Paginator(Denuncia.get_all(request.args), Configuracion.getConfigs().maxElementos, request.args.get("page", 0)))

def show(id):
    """Obtener y mostrar una denuncia para gestionar"""
    if not authenticated(session) or not check_permission(session["id"], "denuncia_update"):
        abort(401)

    return render_template("denuncia/show.html", denuncia=Denuncia.query.get_or_404(id))

def set_status():
    """Método para setear un estado a la denuncia"""
    if not authenticated(session) or not check_permission(session["id"], "denuncia_update") and (request.form["status"] == '' and request.form["id"] == ''):
        abort(401)

    if not request.form["status"] in status_names:
        abort(500)

    denuncia = Denuncia.query.get_or_404(request.form["id"])
    
    denuncia.status = request.form["status"]

    # En caso de que se re-abra la denuncia, borrar la fecha de clsed_at
    if(request.form["status"] == "CLOSED"):
        denuncia.closed_at = datetime.now()
    else:
        denuncia.closed_at = ""
    

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

    denuncia = Denuncia.query.get_or_404(request.form["id"])

    if denuncia.status == "CLOSED":
        flash("Esta denuncia está cerrada. Debe reabrirla para poder gestionarla.")
        return redirect(url_for("denuncia_show", id = request.form["id"]))

    db.session.add(
        Seguimiento(
            denuncia_id = denuncia.id,
            author_id = session["id"],
            created_at = datetime.now(),
            description = request.form["seguimiento"]
        )
    )

    try:
        db.session.commit()
        flash("Seguimiento de denuncia actualizado")
    except Exception as e:
        print(e)
        flash("Error")

    return redirect(url_for('denuncia_show', id = request.form["id"]))

def new_denuncia():
    """Método para usar en la API"""
    postdata = request.get_json()

    try:
        validate_email(postdata["email_denunciante"])
    except EmailNotValidError:
        return "Email inválido"

    try:
        int(postdata["categoria_id"])
    except:
        return "ID de categoría inválido"
    
    Categoria.query.get_or_404(postdata["categoria_id"])

    if postdata["coordenadas"] == '':
        return response.Response(status=500)

    if postdata["apellido_denunciante"] == '':
        return response.Response(status=500)

    if postdata["nombre_denunciante"] == '':
        return response.Response(status=500)

    if postdata["telcel_denunciante"] == '':
        return response.Response(status=500)

    if postdata["titulo"] == '':
        return response.Response(status=500)

    if postdata["descripcion"] == '':
        return response.Response(status=500)

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

