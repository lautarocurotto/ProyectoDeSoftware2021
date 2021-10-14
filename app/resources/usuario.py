from datetime import datetime
from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import db
from datetime import datetime


#from app.helpers.auth import authenticated
from app.models.usuario import Usuario
from app.models.usuario_tiene_rol import usuario_tiene_rol
from app.resources.validadorUsuarios import ValidarForm
from app.models.configuracion import Configuracion

# Protected resources
def index():
    #if not authenticated(session):
     #   abort(401)
    conf=Configuracion.getConfigs()
    params=request.args
    currentPage = int(params.get("page", 0))
    usuariosTotal = Usuario.dame_todo(conf,currentPage,params.get("statusF",None),params.get("nombreF",None))
    return render_template("usuarios/usuarios.html", filtroStatus=params.get("statusF",None), usuarios=usuariosTotal, nextPage=currentPage+1, prevPage=currentPage-1, max=conf.maxElementos)


def create():
    #if not authenticated(session):
     #   abort(401)
    params=request.form
    mensaje=ValidarForm(params)
    if mensaje.validate()==False:
        print("Hay algo mal en el formulario") # En realidad aca se haria un abort ya que algun dato esta mal ingresado
    else:
        email=params['email']
        username=params['username']
        existeMail= Usuario.find_by_email(email)
        existeUserName= Usuario.find_by_username(username)
        now=datetime.now()
        if(existeMail==0 and existeUserName==0):   
            new_usuario=Usuario(email=params["email"],username=params["username"],password=params["password"],activo=int(params["status"]),updated_at=now,created_at=now,first_name=params["name"],last_name=params["lastname"])
            db.session.add(new_usuario)
            db.session.commit()
            rol=usuario_tiene_rol(usuario_id=new_usuario.id,rol_id=int(params["rol"]))
            db.session.add(rol)
            db.session.commit()
            mensaje="Se agrego el usuario"
        else:
            if(existeMail!=0):
                mensaje="El mail ya esta en uso, elija otro"
            if(existeUserName!=0):
                mensaje="El nombre de usuario ya esta en uso, elija otro"
        flash(mensaje)    
    return redirect(url_for("usuario_index"))


def update(id):
    usuario_to_update=Usuario.find_by_id(id)
    if request.method == 'POST':
        params=request.form
        mensaje=ValidarForm(params)
        if mensaje.validate()==False:
            print("Hay algo mal en el formulario") # En realidad aca se haria un abort ya que algun dato esta mal ingresado
            return render_template("usuarios/update.html", usuario=usuario_to_update)
        else:
            existeMail=Usuario.existe_mail(params["email"],id)
            existeUsername=Usuario.existe_username(params["username"],id)
            if(existeMail==0 and existeUsername==0): 
                usuario_to_update.email=params["email"]
                usuario_to_update.username=params["username"]
                usuario_to_update.password=params["password"]
                usuario_to_update.updated_at=datetime.now()
                usuario_to_update.first_name=params["name"]
                usuario_to_update.last_name=params["lastname"]
                usuario_to_update.activo=int(params["status"])
                db.session.commit()
                flash("El usuario se ha modificado con exito")
                return redirect(url_for("usuario_index"))
            else:
                if(existeMail!=0):
                    mensaje="El mail ingresado ya existe"
                if(existeUsername!=0):
                    mensaje="El nombre de usuario ingresado ya existe"
                flash(mensaje)
                return render_template("usuarios/update.html",usuario=usuario_to_update)
    else:
        return render_template("usuarios/update.html",usuario=usuario_to_update)


def delete(id):
    usuario_to_delete=Usuario.find_by_id(id)
    if(usuario_to_delete.activo==0):
        mensaje="el usuario ya se encuentra borrado"
    else:
        esAdministrador=usuario_tiene_rol.find_by_id(id)
        if(esAdministrador!=0):
            mensaje="no se puede eliminar a un usuario administrador"
        else:
            usuario_to_delete.activo=0
            db.session.commit()
            mensaje="El usuario se ha eliminado con exito"
    flash(mensaje)
    return redirect(url_for("usuario_index"))


    
    

        
      


        






