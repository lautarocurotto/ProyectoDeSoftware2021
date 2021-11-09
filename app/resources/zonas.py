from flask import redirect, render_template, request, url_for, session, abort
import flask
from flask.helpers import flash
from sqlalchemy.sql.expression import true
from app.db import db
from app.db import connection
from app.resources.validadorPuntos import ValidarForm

from app.helpers.auth import authenticated, check_permission
from app.helpers.paginator import Paginator
from app.models.zonas import Zonas
from app.models.configuracion import Configuracion

# Protected resources

 
def index():
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    if (not check_permission(session["id"],"zonas_index")):
       abort(401)
    conf=Configuracion.get_configs()
    params=request.args
    currentPage = int(params.get("page", 0))

    puntosTotal = Zonas.dame_todo(conf,params.get("nombreF",None),params.get("statusF",None))

    return render_template("zonas/zonas.html", paginator=Paginator(puntosTotal, conf.maxElementos, currentPage))

def show(id):

    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    if (not check_permission(session["id"],"zonas_show")):
       abort(401)
    z=Zonas.query.get_or_404(id)

    return render_template("zonas/show.html", zonas=z)

def delete(id):
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    if (not check_permission(session["id"],"zonas_destroy")):
       abort(401)
    zona_to_delete=Zonas.find_by_id(id)
    if(zona_to_delete.estado=="despublicado"):
        mensaje="el usuario ya se encuentra borrado"
    else:
        zona_to_delete.estado="despublicado"
        db.session.commit()
        mensaje="La zona innundable se ha eliminado con exito"
    flash(mensaje)
    return redirect(url_for("zonas_index"))

def activar(id):
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    
    zona_to_activate=Zonas.find_by_id(id)
    if(zona_to_activate.estado=="publicado"):
        mensaje="La zona ya se encuentra activada"
    else:
        zona_to_activate.estado="publicado"
        db.session.commit()
        mensaje="La zona se ha activado con exito"
    flash(mensaje)
    return redirect(url_for("zonas_index"))
