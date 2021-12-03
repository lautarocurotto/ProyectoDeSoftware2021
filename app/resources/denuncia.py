from datetime import datetime
from flask import redirect, render_template, request, url_for, session, abort, flash
from app.models.denuncia import Denuncia
from app.helpers.paginator import Paginator
from app.models.configuracion import Configuracion
from app.helpers.auth import authenticated, check_permission
from app.models.seguimiento import Seguimiento
from app.models.categoria import Categoria
from app.models.usuario import Usuario
from email_validator import validate_email, EmailNotValidError

from app.db import db

status_names = ["UNCONFIRMED", "IN_PROGRESS", "RESOLVED", "CLOSED"]


def index():
    """Obtener y mostrar todas las denuncias"""

    if not authenticated(session) or not check_permission(
        session["id"], "denuncia_index"
    ):
        abort(401)

    return render_template(
        "denuncia/denuncias.html",
        paginator=Paginator(
            Denuncia.get_all(request.args),
            Configuracion.get_configs().maxElementos,
            int(request.args.get("page", 0)),
        ),
        categorias=Categoria.query.all(),
    )


def show(id):
    """Obtener y mostrar una denuncia para gestionar"""

    if not authenticated(session) or not check_permission(
        session["id"], "denuncia_update"
    ):
        abort(401)

    categorias = []

    if not request.args.get("edit-categoria") == None:
        categorias = Categoria.query.all()

    return render_template(
        "denuncia/show.html",
        denuncia=Denuncia.query.get_or_404(id),
        categorias=categorias,
    )


def update_seguimiento():
    if (
        not authenticated(session)
        or not check_permission(session["id"], "denuncia_update")
        and (request.form["seguimientos"] == "" and request.form["id"] == "")
    ):
        abort(401)

    denuncia = Denuncia.query.get_or_404(request.form["id"])

    if denuncia.status == "CLOSED":
        flash("Esta denuncia está cerrada. Debe reabrirla para poder gestionarla.")
        return redirect(url_for("denuncia_show", id=request.form["id"]))

    db.session.add(
        Seguimiento(
            denuncia_id=denuncia.id,
            author_id=session["id"],
            created_at=datetime.now(),
            description=request.form["seguimiento"],
        )
    )

    try:
        db.session.commit()
        flash("Seguimiento de denuncia actualizado")
    except Exception as e:
        print(e)
        flash("Error")

    return redirect(url_for("denuncia_show", id=request.form["id"]))


def new_denuncia():
    """Método para usar con form"""

    postdata = request.form

    datos_usuario = Usuario.query.get_or_404(session["id"])

    try:
        int(postdata["categoria_id"])
    except:
        flash("Categoría inválida")
        return redirect(url_for("denuncias"))

    Categoria.query.get_or_404(postdata["categoria_id"])

    if postdata["lat"] == "" or postdata["lng"] == "":
        flash("Debe introducir coordenadas")
        return redirect(url_for("denuncias"))

    if postdata["titulo"] == "":
        flash("Título inválido")
        return redirect(url_for("denuncias"))

    if postdata["descripcion"] == "":
        flash("Descripción inválida")
        return redirect(url_for("denuncias"))

    db.session.add(
        Denuncia(
            category_id=postdata["categoria_id"],
            coordenada_lat=postdata["lat"],
            coordenada_lng=postdata["lng"],
            denunciante_name=datos_usuario.first_name,
            denunciante_last_name=datos_usuario.last_name,
            denunciante_phone="User " + datos_usuario.username,
            denunciante_email=datos_usuario.email,
            title=postdata["titulo"],
            description=postdata["descripcion"],
            status="IN_PROGRESS",
        )
    )

    try:
        db.session.commit()
    except Exception as e:
        return str(e)

    flash("Denuncia creada")
    return redirect(url_for("denuncias"))


def delete_denuncia():
    postdata = request.form

    if not authenticated(session) or not check_permission(
        session["id"], "denuncia_destroy"
    ):
        abort(401)

    if postdata["id"] == "":
        flash("Error!")
        return redirect(url_for("denuncias"))

    try:
        db.session.delete(Denuncia.query.get_or_404(postdata["id"]))
        db.session.commit()
        flash("Denuncia eliminada.")
        return redirect(url_for("denuncias"))
    except:
        flash("Error")
        return redirect(url_for("denuncias"))


def set_coordenadas():
    if not authenticated(session) or not check_permission(
        session["id"], "denuncia_update"
    ):
        abort(401)

    postdata = request.form

    denuncia = Denuncia.query.get_or_404(postdata["id"])
    denuncia.coordenada_lat = postdata["lat"]
    denuncia.coordenada_lng = postdata["lng"]

    try:
        db.session.commit()
        flash("Coordenadas actualizadas")
    except:
        flash("Error al intentar actualizar el mapa")

    return redirect(url_for("denuncia_show", id=request.form["id"]))


# ============================== SETTERS ==========================================


def set_descripcion():
    if not authenticated(session) or not check_permission(
        session["id"], "denuncia_update"
    ):
        abort(401)

    postdata = request.form

    denuncia = Denuncia.query.get_or_404(postdata["id"])
    denuncia.description = postdata["descripcion"]

    try:
        db.session.commit()
        flash("Descripción actualizada")
    except:
        flash("Error al intentar actualizar la descripción")

    return redirect(url_for("denuncia_show", id=request.form["id"]))


def set_denunciante():
    if not authenticated(session) or not check_permission(
        session["id"], "denuncia_update"
    ):
        abort(401)

    postdata = request.form

    if postdata["id"] == "":
        flash("Error!")
        return redirect(url_for("denuncias"))

    denuncia = Denuncia.query.get_or_404(postdata["id"])

    if postdata["denunciante_name"] != "":
        denuncia.denunciante_name = postdata["denunciante_name"]

    if postdata["denunciante_last_name"] != "":
        denuncia.denunciante_last_name = postdata["denunciante_last_name"]

    if postdata["denunciante_email"] != "":
        try:
            validate_email(postdata["denunciante_email"])
            denuncia.denunciante_email = postdata["denunciante_email"]
        except EmailNotValidError:
            flash("Email inválido")
            return redirect(url_for("denuncia_show", id=postdata["id"]))

    if postdata["denunciante_phone"] != "":
        denuncia.denunciante_phone = postdata["denunciante_phone"]

    try:
        db.session.commit()
        flash("Denunciante actualizado")
    except:
        flash("Error")

    return redirect(url_for("denuncia_show", id=postdata["id"]))


def set_status():
    """Método para setear un estado a la denuncia"""
    if (
        not authenticated(session)
        or not check_permission(session["id"], "denuncia_update")
        and (request.form["status"] == "" and request.form["id"] == "")
    ):
        abort(401)

    if not request.form["status"] in status_names:
        abort(500)

    denuncia = Denuncia.query.get_or_404(request.form["id"])

    denuncia.status = request.form["status"]

    # En caso de que se re-abra la denuncia, borrar la fecha de clsed_at
    if request.form["status"] == "CLOSED":
        denuncia.closed_at = datetime.now()
    else:
        denuncia.closed_at = ""

    try:
        db.session.commit()
        flash("Estado de denuncia actualizado")
    except Exception as e:
        print("Error @ denuncia#set_status()")
        print(e)
        flash("Fin Error @ denuncia#set_status()")

    return redirect(url_for("denuncia_show", id=request.form["id"]))


def set_categoria():
    if (
        not authenticated(session)
        or not check_permission(session["id"], "denuncia_update")
        and request.form["id"] == ""
    ):
        abort(401)

    postdata = request.form

    if postdata["categoria"] != "":
        Denuncia.query.get_or_404(request.form["id"]).category_id = postdata[
            "categoria"
        ]

    try:
        db.session.commit()
        flash("Categoría actualizada")
    except:
        flash("Error!")

    return redirect(url_for("denuncia_show", id=request.form["id"]))
