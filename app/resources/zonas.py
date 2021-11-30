from flask import redirect, render_template, request, url_for, session, abort
import flask
from flask.helpers import flash
from sqlalchemy.sql.expression import true
from app.db import db
from app.db import connection
from app.models.coordenadas import Coordenadas
from app.resources.validadorPuntos import ValidarForm

from app.helpers.auth import authenticated, check_permission
from app.helpers.paginator import Paginator
from app.models.zonas import Zonas
from app.models.configuracion import Configuracion
import csv
import io
import uuid

# Protected resources


def index():
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "zonas_index"):
        abort(401)
    conf = Configuracion.get_configs()
    params = request.args
    currentPage = int(params.get("page", 0))

    puntosTotal = Zonas.dame_todo(
        conf, params.get("nombreF", None), params.get("statusF", None)
    )

    return render_template(
        "zonas/zonas.html",
        paginator=Paginator(puntosTotal, conf.maxElementos, currentPage),
    )


def show(id):

    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "zonas_show"):
        abort(401)
    z = Zonas.query.get_or_404(id)

    return render_template("zonas/show.html", zonas=z)


def delete(id):
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "zonas_destroy"):
        abort(401)
    zona_to_delete = Zonas.find_by_id(id)
    if zona_to_delete.estado == "despublicado":
        mensaje = "La zona inundable ya se encuentra despublicada"
    else:
        zona_to_delete.estado = "despublicado"
        db.session.commit()
        mensaje = "La zona innundable se ha despublicado con exito"
    flash(mensaje)
    return redirect(url_for("zonas_index"))


def activar(id):
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "zonas_destroy"):
        abort(401)
    zona_to_activate = Zonas.find_by_id(id)
    if zona_to_activate.estado == "publicado":
        mensaje = "La zona ya se encuentra activada"
    else:
        zona_to_activate.estado = "publicado"
        db.session.commit()
        mensaje = "La zona se ha activado con exito"
    flash(mensaje)
    return redirect(url_for("zonas_index"))


def allowedfile(file):
    allowed_extension = {"csv"}
    return "." in file and file.rsplit(".", 1)[1].lower() in allowed_extension


def cantidad_puntos(id):
    return Zonas.cant_puntos(id)


def importar():
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "zonas_import"):
        abort(401)
    if request.method == "POST":
        filename = request.files["archivo"].filename
        if not (filename and allowedfile(filename)):
            mensaje = "No se ingresó un archivo .csv"
            flash(mensaje)
            return redirect(url_for("zonas_index"))
        arch = request.files["archivo"].read()
        archi = arch.decode()
        mycsv = io.StringIO(archi)
        reader = csv.DictReader(mycsv)
        for row in reader:
            codigo = str(uuid.uuid4())
            nombre = row["name"]
            if not Zonas.existe_zona(nombre):
                new_zona = Zonas(
                    codigo=codigo, nombre=nombre, estado="publicado", color="#ff0000"
                )
            else:
                new_zona = Zonas.get_by_name(nombre)
                for coordenadas_to_delete in new_zona.puntos:
                    db.session.delete(coordenadas_to_delete)
                db.session.commit()
            areas = row["area"]
            stri = areas.split(",")
            for i in range(len(stri)):
                if i % 2 == 0:
                    lat = stri[i].replace("[", "")
                    print(lat)
                else:
                    lng = stri[i].replace("]", "")
                    print(lng)
                    new_coordenada = Coordenadas(lat=lat, lng=lng, tipo="zonas")
                    new_zona.puntos.append(new_coordenada)
            db.session.add(new_zona)
            db.session.commit()
    return redirect(url_for("zonas_index"))


def delete_fisico(id):
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "zonas_destroy"):
        abort(401)
    zona_to_delete = Zonas.find_by_id(id)
    try:
        db.session.delete(zona_to_delete)
        db.session.commit()
        mensaje = "Se eliminó con éxito"
        flash(mensaje)
        return redirect(url_for("zonas_index"))
    except:
        return "Hubo un problema al borrar el recorrido de evacuacion"
