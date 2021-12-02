from app.models.configuracion import Configuracion
from flask import render_template, request, abort, redirect, url_for, flash, session
from app.db import db
from app.helpers.auth import authenticated, check_permission


def index():
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "configuracion_update"):
        abort(401)
    return render_template("configuration.html")


def get_configs():
    return Configuracion.get_configs()


def set_configs():
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "usuario_show"):
        abort(401)
    postdata = request.form

    current_configs = Configuracion.get_configs()

    if postdata["color1"] != None:
        current_configs.color1Privada = postdata["color1"]

    if not postdata["color2"] == None:
        current_configs.color2Privada = postdata["color2"]

    if not postdata["color3"] == None:
        current_configs.color3Privada = postdata["color3"]

    if not postdata["max-elementos"] == None:
        try:
            new_max_elementos = int(postdata["max-elementos"])
            current_configs.maxElementos = new_max_elementos
        except:
            flash("Cantidad de elementos inválida")
            abort(500)

    if not postdata["criterio"] == None:
        current_configs.criterio_orden = postdata["criterio"]

    try:
        db.session.commit()
        flash("Configuración actualizada")
        return redirect(url_for("configuracion"))
    except:
        return "Error al intentar configurar el sitio"


def toggleMaintenance():
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "usuario_show"):
        abort(401)

    current_configs = Configuracion.get_configs()
    current_mantenimiento = current_configs.sitio_en_mantenimiento
    current_configs.sitio_en_mantenimiento = not (current_mantenimiento)
    try:
        db.session.commit()
        if current_mantenimiento:
            flash("Sitio publicado. Estamos en vivo")
        else:
            flash("Sitio puesto en mantenimiento")

        return redirect(url_for("configuracion"))
    except:
        return "Error al intentar configurar el sitio"
