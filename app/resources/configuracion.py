from sqlalchemy.sql.functions import current_timestamp
from app.models.configuracion import Configuracion
from flask import render_template, request , abort, redirect, url_for, flash
from app.db import db

def index():
    configs = Configuracion.query.all()
    return render_template("configuration.html", configs=configs)

def setColor1():
    postdata = request.form
    if(not postdata["color1"] == None):
        Configuracion.query.all()[0].color1Privada = postdata["color1"]
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
        Configuracion.query.all()[0].color2Privada = postdata["color2"]
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
        Configuracion.query.all()[0].color3Privada = postdata["color3"]
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
        Configuracion.query.all()[0].maxElementos = postdata["max-elementos"]
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
        Configuracion.query.all()[0].criterio_orden = postdata["criterio"]
        try:
            db.session.commit()
            flash("Criterio de ordenación actualizado.")
            return redirect(url_for("configuracion"))
        except:
            return "Hubo un problema al actualizar el criterio de ordenación"
    else:
        abort(404)

def toggleMaintenance():
    current_mantenimiento = Configuracion.query.all()[0].sitio_en_mantenimiento
    Configuracion.query.all()[0].sitio_en_mantenimiento = not (current_mantenimiento)
    try:
        db.session.commit()
        if(current_mantenimiento):
            flash("Sitio publicado. Estamos en vivo")
        else:
           flash("Sitio puesto en mantenimiento") 
        
        return redirect(url_for("configuracion"))
    except:
        return "El mantenimiento es " + str(current_mantenimiento) + "\n <a href=\"{{url_for('configuration')}}\">Volver</a>"
