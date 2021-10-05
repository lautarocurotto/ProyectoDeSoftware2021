from flask import redirect, render_template, request, url_for, session, abort
from app.db import db

#from app.helpers.auth import authenticated
from app.models.punto import Punto

# Protected resources
def index():
    #if not authenticated(session):
     #   abort(401)

    puntosTotal = Punto.query.all()
    return render_template("puntos-encuentro.html", puntos=puntosTotal)
    


def create():
    #if not authenticated(session):
     #   abort(401)
    params=request.form
    new_punto=Punto(nombre=params["nombre"],direccion=params["direccion"],coordenadas=params["coordenadas"],estado=params["status"],telefono=params["telefono"],email=params["email"])
    db.session.add(new_punto)
    db.session.commit()

    return redirect(url_for("puntos_index"))
    
def destroy(id_punto):
    #if not authenticated(session) or not admin(session):
     #   abort(401)

    
    return redirect(url_for("puntos_index"))
