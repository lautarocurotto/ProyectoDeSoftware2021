from flask import redirect, render_template, request, url_for, session, abort
import flask
from flask.helpers import flash
from sqlalchemy.sql.expression import true
from app.db import db

#from app.helpers.auth import authenticated
from app.models.punto import Punto
from app.models.configuracion import Configuracion

# Protected resources
def index():
    #if not authenticated(session):
     #   abort(401)
    conf=Configuracion.getConfigs()
    params=request.args
    currentPage = int(params.get("page", 0))
    puntosTotal = Punto.dame_todo(conf,params.get("nombreF",None),params.get("statusF",None), currentPage)
    return render_template("puntos/puntos.html", puntos=puntosTotal, nextPage=currentPage+1, prevPage=currentPage-1, max=conf.maxElementos)
    

def create():
    #if not authenticated(session):
     #   abort(401)
    params=request.form
    cant_puntos=Punto.existe_punto(params["nombre"])
    if (cant_puntos==0):
        new_punto=Punto(nombre=params["nombre"],direccion=params["direccion"],coordenadas=params["coordenadas"],estado=params["status"],telefono=params["telefono"],email=params["email"])
        db.session.add(new_punto)
        db.session.commit()
        mensaje="Se agrego el punto"
    else:
        mensaje="El punto ya existe por favor elija otro nombre"
    flash(mensaje)
    return redirect(url_for("puntos_index"))

def update(id):
    #if not authenticated(session):
     #   abort(401)

    punto_to_update=Punto.query.get_or_404(id)
    if request.method == "POST":
        params=request.form
        cant_puntos=Punto.existe_punto(params["nombre"])
        if (cant_puntos==0):
            punto_to_update.nombre=params["nombre"]
            punto_to_update.direccion=params["direccion"]
            punto_to_update.coordenadas=params["coordenadas"]
            punto_to_update.estado=params["status"]
            punto_to_update.telefono=params["telefono"]
            punto_to_update.email=params["email"]
            try:
                db.session.commit()
                return redirect(url_for("puntos_index"))
            except:
                flash ("Hubo un problema al actualizar el punto de encuento")
                return render_template("puntos/.html", punto_to_update=punto_to_update)
        else:
            flash("El nombre ya existe, por favor elija otro nombre")
            return render_template("puntos/update.html", punto_to_update=punto_to_update)
    else:
        return render_template("puntos/update.html", punto_to_update=punto_to_update)
    

def delete(id):
    #if not authenticated(session) or not admin(session):
     #   abort(401)

    punto_to_delete=Punto.query.get_or_404(id)
    try:
        db.session.delete(punto_to_delete)
        db.session.commit()
        return redirect(url_for("puntos_index"))
    except:
        return "Hubo un problema al borrar el punto de encuento"

def show(id):
    #if not authenticated(session) or not admin(session):
     #   abort(401)

    p=Punto.query.get_or_404(id)

    return render_template("puntos/show.html", punto=p)
   
        

    
