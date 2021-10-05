from flask import redirect, render_template, request, url_for, session, abort

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

    #conn = connection()
    #Punto.create(conn, request.form)
    return redirect(url_for("punto_index"))
    
def destroy(id_punto):
    #if not authenticated(session) or not admin(session):
     #   abort(401)

    
    return redirect(url_for("punto_index"))
