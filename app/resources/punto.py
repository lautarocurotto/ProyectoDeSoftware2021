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

def update(id):
    #if not authenticated(session):
     #   abort(401)

    punto_to_update=Punto.query.get_or_404(id)
    if request.method == "POST":
        params=request.form
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
            return "Hubo un problema al actualizar el punto de encuento"
    else:
        return render_template("punto-encuentro-update.html", punto_to_update=punto_to_update)
    

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

    
