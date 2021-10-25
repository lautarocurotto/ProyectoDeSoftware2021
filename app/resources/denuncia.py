from flask import redirect, render_template, request, url_for, session, abort, flash
from app.models.denuncia import Denuncia
from app.helpers.paginator import Paginator
from app.models.configuracion import Configuracion
from app.helpers.auth import authenticated, check_permission

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
    try:
        db.session.commit()
        flash("Estado de denuncia actualizado")
    except:
        print("Error @ denuncia#set_status()")
        flash("Error")
    
    return redirect(url_for('denuncia_show', id = request.form["id"]))