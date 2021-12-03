from datetime import datetime
from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import db
from datetime import datetime
from app.models.roles import Rol
from app.models.usuario import Usuario
from app.models.usuario_publico import Usuario_publico
from app.models.usuario_tiene_rol import usuario_tiene_rol
from app.models.configuracion import Configuracion
from app.helpers.auth import authenticated, check_permission
from app.helpers.paginator import Paginator
from email_validator import validate_email, EmailNotValidError



def index():
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    if (not check_permission(session["id"],"usuariopublico_index")):
       abort(401)
    conf=Configuracion.get_configs()
    params=request.args
    currentPage = int(params.get("page", 0))

    usuariosTotal = Usuario_publico.dame_todo(conf,currentPage)
    return render_template("usuariopublico/usuarios.html", paginator=Paginator(usuariosTotal, conf.maxElementos, currentPage))

def activar(id):
    user = authenticated(session)
    if (not user):
        return redirect(url_for("auth_login"))
    if (not check_permission(session["id"],"usuariopublico_activar")):
       abort(401)
    usuario_to_activate=Usuario_publico.find_by_id(id)
    new_usuario=Usuario(email=usuario_to_activate.email,username=None,password=None,activo=1,updated_at=datetime.now(),created_at=datetime.now(),first_name=usuario_to_activate.first_name,last_name=usuario_to_activate.last_name)
    db.session.add(new_usuario)
    db.session.commit()
    db.session.delete(usuario_to_activate)
    db.session.commit()
    rol1=usuario_tiene_rol(usuario_id=new_usuario.id,rol_id=1)
    db.session.add(rol1)
    db.session.commit()
    flash("Usuario activado")
    return redirect(url_for("usuariopublico_index"))


