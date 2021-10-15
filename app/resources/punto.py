from flask import redirect, render_template, request, url_for, session, abort
import flask
from flask.helpers import flash
from sqlalchemy.sql.expression import true
from app.db import db
from app.resources.validadorPuntos import ValidarForm

from app.helpers.auth import authenticated
from app.models.punto import Punto
from app.models.configuracion import Configuracion

# Protected resources

 
def index():
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    conf=Configuracion.getConfigs()
    params=request.args
    currentPage = int(params.get("page", 0))
    puntosTotal = Punto.dame_todo(conf,params.get("nombreF",None),params.get("statusF",None), currentPage)
    return render_template("puntos/puntos.html", filtroStatus=params.get("statusF",None), puntos=puntosTotal, nextPage=currentPage+1, prevPage=currentPage-1, max=conf.maxElementos)
    

def create():
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    params=request.form
    mensaje=ValidarForm(params)
    if mensaje.validate()==False:
        print("Hay algo mal en el formulario") # En realidad aca se haria un abort ya que algun dato esta mal ingresado
    else:
        print("Los campos estan validados")
        cant_puntos=Punto.existe_punto(params["nombre"]) # Me fijo si ya existe un punto con ese nombre
        if (cant_puntos==0): #si la cantidad es 0 es porque no hay ninguna tupla en la base de datos con ese nombre, o sea que no existe 
            new_punto=Punto(nombre=params["nombre"],direccion=params["direccion"],coordenadas=params["coordenadas"],estado=params["status"],telefono=params["telefono"],email=params["email"])
            db.session.add(new_punto)
            db.session.commit()
            mensaje="Se agrego el punto"
        else:
            mensaje="El punto ya existe por favor elija otro nombre"
        flash(mensaje)
    return redirect(url_for("puntos_index"))

def update(id):

    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    params=request.form
    punto_to_update=Punto.query.get_or_404(id)
    if request.method == "POST":
        mensaje=ValidarForm(params)
        if mensaje.validate()==False:
            print("Hay algo mal en el formulario") # En realidad aca se haria un abort ya que algun dato esta mal ingresado
            return render_template("puntos/update.html", punto_to_update=punto_to_update)
        else:
            print("Los campos estan validados")
            cant_puntos=Punto.existe_punto(params["nombre"],id,True)
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
                    return render_template("puntos/update.html", punto_to_update=punto_to_update)
            else:
                flash("El nombre ya existe, por favor elija otro nombre")
                return render_template("puntos/update.html", punto_to_update=punto_to_update)
    else:
        return render_template("puntos/update.html", punto_to_update=punto_to_update)
    

def delete(id):
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    #or not admin    
    punto_to_delete=Punto.query.get_or_404(id)
    try:
        db.session.delete(punto_to_delete)
        db.session.commit()
        return redirect(url_for("puntos_index"))
    except:
        return "Hubo un problema al borrar el punto de encuento"

def show(id):

    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    #or not admin    

    p=Punto.query.get_or_404(id)

    return render_template("puntos/show.html", punto=p)
   
        

    
