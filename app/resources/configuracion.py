from sqlalchemy.sql.functions import current_timestamp
from app.models.configuracion import Configuracion
from flask import render_template, request , abort, redirect, url_for, flash
from app.db import db

def index():
    return render_template("configuration.html")

def getConfigs():
    return Configuracion.getConfigs()

def setColor1():
    postdata = request.form
    if(not postdata["color1"] == None):
        Configuracion.getConfigs().color1Privada = postdata["color1"]
        try:
            db.session.commit()
            flash("Paleta de colores actualizada")
            return redirect(url_for("configuracion"))
        except:
            return "Hubo un problema al actualizar el punto de encuento"
    else:
        abort(404)


def setColor2():
    postdata = request.form
    if(not postdata["color2"] == None):
        Configuracion.getConfigs().color2Privada = postdata["color2"]
        try:
            db.session.commit()
            flash("Paleta de colores actualizada")
            return redirect(url_for("configuracion"))
        except:
            return "Hubo un problema al actualizar el punto de encuento"
    else:
        abort(404)

def setColor3():
    postdata = request.form
    if(not postdata["color3"] == None):
        Configuracion.getConfigs().color3Privada = postdata["color3"]
        try:
            db.session.commit()
            flash("Paleta de colores actualizada")
            return redirect(url_for("configuracion"))
        except:
            return "Hubo un problema al actualizar el punto de encuento"
    else:
        abort(404)

def setMaxElementos():
    postdata = request.form
    if(not postdata["max-elementos"] == None):
        Configuracion.getConfigs().maxElementos = postdata["max-elementos"]
        try:
            db.session.commit()
            flash("Cantidad de elementos configurados.")
            return redirect(url_for("configuracion"))
        except Exception as e:
            return str(e)
    else:
        abort(404)

def setCriterioOrden():
    postdata = request.form
    if(not postdata["criterio"] == None):
        Configuracion.getConfigs().criterio_orden = postdata["criterio"]
        try:
            db.session.commit()
            flash("Criterio de ordenación actualizado.")
            return redirect(url_for("configuracion"))
        except:
            return "Hubo un problema al actualizar el criterio de ordenación"
    else:
        abort(404)

def toggleMaintenance():
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
