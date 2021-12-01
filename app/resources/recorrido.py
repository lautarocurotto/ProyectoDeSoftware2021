from flask import redirect, render_template, request, url_for, session, abort
from flask.helpers import flash
from app.db import db
from app.models.coordenadas import Coordenadas
from app.helpers.auth import authenticated, check_permission
from app.helpers.paginator import Paginator
from app.models.recorrido import Recorrido
from app.models.configuracion import Configuracion
from app.validadores.validadorRecorridos import ValidarForm

# Protected resources


def index():
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "recorrido_index"):
        abort(401)
    conf = Configuracion.get_configs()
    params = request.args
    currentPage = int(params.get("page", 0))

    recorridosTotal = Recorrido.dame_todo(
        conf, params.get("nombreF", None), params.get("statusF", None)
    )

    return render_template(
        "recorridos/recorridos.html",
        paginator=Paginator(recorridosTotal, conf.maxElementos, currentPage),
    )


def create():
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "recorrido_new"):
        abort(401)

    contenido = request.get_json()
    nombree = contenido["name"]
    descripcionn = contenido["description"]
    estadoo = contenido["status"]
    coordendas = contenido["coodinates"]
    respuesta=ValidarForm.validar(nombree,descripcionn,estadoo,coordendas)
    if respuesta=="Todo ok":
        print("Los campos estan validados")
        cant_puntos = Recorrido.existe_recorrido(nombree)
        if cant_puntos == 0:
            new_recorrido = Recorrido(
                nombre=nombree, descripcion=descripcionn, estado=estadoo)
            for c in coordendas:
                new_coordenada = Coordenadas(
                   lat=c["lat"], lng=c["lng"], tipo="recorrido")
                new_recorrido.puntos.append(new_coordenada)
                db.session.add(new_recorrido)
                db.session.commit()
                mensaje = "Se agrego el recorrido"
        else:
            mensaje = "El recorrido ya existe por favor elija otro nombre"
        flash(mensaje)
    return redirect(url_for("recorridos_index"))


def update(id):
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "recorrido_update"):
        abort(401)
    recorrido_to_update = Recorrido.query.get_or_404(id)
    return render_template(
        "recorridos/update.html", recorrido_to_update=recorrido_to_update
    )


def updateCurrent():
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "recorrido_update"):
        abort(401)

    contenido = request.get_json()
    print(contenido)
    nombree = contenido["name"]
    descripcionn = contenido["description"]
    estadoo = contenido["status"]
    coordendas = contenido["coodinates"]
    recorrido_to_update = Recorrido.query.get_or_404(contenido["id"])
    if nombree == "" or descripcionn == "" or estadoo == "" or len(coordendas) < 3:
        print("Hay algo mal en el formulario")
        return render_template(
            "puntos/update.html", recorrido_to_update=recorrido_to_update
        )
    else:
        print("Los campos estan validados")
        cant_puntos = Recorrido.existe_recorrido(
            contenido["name"], contenido["id"], True
        )
        if cant_puntos == 0:
            recorrido_to_update.nombre = contenido["name"]
            recorrido_to_update.descripcion = contenido["description"]
            recorrido_to_update.estado = contenido["status"]
            for c in recorrido_to_update.puntos:
                db.session.delete(c)
            for c in coordendas:
                new_coordenada = Coordenadas(
                    lat=c["lat"], lng=c["lng"], tipo="recorrido"
                )
                recorrido_to_update.puntos.append(new_coordenada)
            try:
                db.session.commit()
                return redirect(url_for("recorridos_index"))
            except:
                flash("Hubo un problema al actualizar el recorrido de evacuacion")
                return render_template(
                    "recorridos/update.html", recorrido_to_update=recorrido_to_update
                )
        else:
            flash("El nombre ya existe, por favor elija otro nombre")
            return render_template(
                "recorridos/update.html", recorrido_to_update=recorrido_to_update
            )


def delete(id):
    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "recorrido_destroy"):
        abort(401)
    recorrido_to_delete = Recorrido.query.get_or_404(id)
    try:
        db.session.delete(recorrido_to_delete)
        db.session.commit()
        return redirect(url_for("recorridos_index"))
    except:
        return "Hubo un problema al borrar el recorrido de evacuacion"


def show(id):

    user = authenticated(session)
    if not user:
        return redirect(url_for("auth_login"))
    if not check_permission(session["id"], "recorrido_show"):
        abort(401)
    r = Recorrido.query.get_or_404(id)

    return render_template("recorridos/show.html", recorrido=r)
