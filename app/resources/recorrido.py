from flask import redirect, render_template, request, url_for, session, abort
import flask
from flask.helpers import flash
from sqlalchemy.sql.expression import true
from app.db import db
from app.validadores.validadorRecorridos import ValidarForm

from app.helpers.auth import authenticated, check_permission
from app.helpers.paginator import Paginator
from app.models.recorrido import Recorrido
from app.models.configuracion import Configuracion

# Protected resources

 
def index():
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    if (not check_permission(session["id"],"recorrido_index")):
       abort(401)
    conf=Configuracion.getConfigs()
    params=request.args
    currentPage = int(params.get("page", 0))

    recorridosTotal = Recorrido.dame_todo(conf,params.get("nombreF",None),params.get("statusF",None))

    return render_template("recorridos/recorridos.html", paginator=Paginator(recorridosTotal, conf.maxElementos, currentPage))
    

def create():
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    if (not check_permission(session["id"],"recorrido_new")):
       abort(401)    
    params=request.form
    mensaje=ValidarForm(params)
    if mensaje.validate()==False:
        print("Hay algo mal en el formulario")
        
    else:
        print("Los campos estan validados")
        cant_puntos=Recorrido.existe_recorrido(params["nombre"]) 
        if (cant_puntos==0): #si la cantidad es 0 es porque no hay ninguna tupla en la base de datos con ese nombre, o sea que no existe 
            new_recorrido=Recorrido(nombre=params["nombre"],descripcion=params["descripcion"],lat=params["lat"],estado=params["status"],lng=params["lng"])
            db.session.add(new_recorrido)
            db.session.commit()
            mensaje="Se agrego el recorrido"
        else:
            mensaje="El recorrido ya existe por favor elija otro nombre"
        flash(mensaje)
    return redirect(url_for("recorridos_index"))

def update(id):

    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    if (not check_permission(session["id"],"recorrido_update")):
       abort(401)
    params=request.form
    recorrido_to_update=Recorrido.query.get_or_404(id)
    if request.method == "POST":
        mensaje=ValidarForm(params)
        if mensaje.validate()==False:
            print("Hay algo mal en el formulario") 
            return render_template("puntos/update.html", recorrido_to_update=recorrido_to_update)
        else:
            print("Los campos estan validados")
            cant_puntos=Recorrido.existe_recorrido(params["nombre"],id,True)
            if (cant_puntos==0):
                recorrido_to_update.nombre=params["nombre"]
                recorrido_to_update.descripcion=params["descripcion"]
                recorrido_to_update.lat=params["lat"]
                recorrido_to_update.estado=params["status"]
                recorrido_to_update.lng=params["lng"]
                try:
                    db.session.commit()
                    return redirect(url_for("recorridos_index"))
                except:
                    flash ("Hubo un problema al actualizar el recorrido de evacuacion")
                    return render_template("recorridos/update.html", recorrido_to_update=recorrido_to_update)
            else:
                flash("El nombre ya existe, por favor elija otro nombre")
                return render_template("recorridos/update.html", recorrido_to_update=recorrido_to_update)
    else:
        return render_template("recorridos/update.html", recorrido_to_update=recorrido_to_update)
    

def delete(id):
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login")) 
    if (not check_permission(session["id"],"recorrido_destroy")):
       abort(401) 
    recorrido_to_delete=Recorrido.query.get_or_404(id)
    try:
        db.session.delete(recorrido_to_delete)
        db.session.commit()
        return redirect(url_for("recorridos_index"))
    except:
        return "Hubo un problema al borrar el recorrido de evacuacion"

def show(id):

    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    if (not check_permission(session["id"],"recorrido_show")):
       abort(401)
    r=Recorrido.query.get_or_404(id)

    return render_template("recorridos/show.html", recorrido=r)