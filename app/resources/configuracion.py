from sqlalchemy.sql.functions import current_timestamp
from app.models.configuracion import Configuracion
from flask import render_template, request , abort, redirect, url_for, flash, session
from app.db import db
from app.helpers.auth import authenticated
from app.helpers import auth

def index():
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    if(auth.isAdmin(session.get("id"))):
        return render_template("configuration.html")

def getConfigs():
    return Configuracion.getConfigs()

def setConfigs():
    if(auth.isAdmin(session.get("id"))):
        postdata = request.form
        if(postdata["color1"] != None):
            Configuracion.getConfigs().color1Privada = postdata["color1"]
        
        if(not postdata["color2"] == None):
            Configuracion.getConfigs().color2Privada = postdata["color2"]
        
        if(not postdata["color3"] == None):
            Configuracion.getConfigs().color3Privada = postdata["color3"]

        if(not postdata["max-elementos"] == None):
            try:
                newMaxElementos = int(postdata["max-elementos"])
                Configuracion.getConfigs().maxElementos = newMaxElementos
            except:
                flash("Cantidad de elementos inválida")
                abort(500)

        if(not postdata["criterio"] == None):
            Configuracion.getConfigs().criterio_orden = postdata["criterio"]

        try:
            db.session.commit()
            flash("Configuración actualizada")
            return redirect(url_for("configuracion"))
        except:
            return "Erro al intentar configurar el sitio"
    else:
        abort(401)


def toggleMaintenance():
    if(auth.isAdmin(session.get("id"))):
        current_mantenimiento = Configuracion.getConfigs().sitio_en_mantenimiento
        Configuracion.getConfigs().sitio_en_mantenimiento = not (current_mantenimiento)
        try:
            db.session.commit()
            if(current_mantenimiento):
                flash("Sitio publicado. Estamos en vivo")
            else:
                flash("Sitio puesto en mantenimiento")

            return redirect(url_for("configuracion"))
        except:
            return "Erro al intentar configurar el sitio"
    else:
        abort(401)
