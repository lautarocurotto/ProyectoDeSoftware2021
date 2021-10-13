from datetime import datetime
from flask import redirect, render_template, request, url_for, session, abort, flash
from app.db import db
from datetime import datetime


#from app.helpers.auth import authenticated
from app.models.usuario import Usuario

# Protected resources
def index():
    #if not authenticated(session):
     #   abort(401)
    params=request.args
    usuariosTotal = Usuario.dame_todo(params.get("statusF",None))
    return render_template("usuarios.html", usuarios=usuariosTotal)

def create():
    #if not authenticated(session):
     #   abort(401)
    params=request.form 
    email=params['email']
    username=params['username']
    existeMail= Usuario.find_by_email(email)
    existeUserName= Usuario.find_by_username(username)
    now=datetime.now()
    if(existeMail==0 and existeUserName==0):   
        new_usuario=Usuario(email=params["email"],username=params["username"],password=params["password"],activo=1,updated_at=now,created_at=now,first_name=params["name"],last_name=params["lastname"])
        db.session.add(new_usuario)
        db.session.commit()
        mensaje="Se agrego el usuario"
    else:
        if(existeMail!=0):
            mensaje="El mail ya esta en uso, elija otro"
        if(existeUserName!=0):
            mensaje="El nombre de usuario ya esta en uso, elija otro"
    flash(mensaje)    
    return redirect(url_for("usuario_index"))

def delete(id):
    usuario_to_delete=Usuario.find_by_id(id)
    usuario_to_delete.activo=False
    db.session.commit()
    return redirect(url_for("puntos_index"))

def update(id):
    usuario_to_update=Usuario.find_by_id(id)
    if request.method == 'POST':
        params=request.form
        existeMail= Usuario.find_by_email(params["email"])
        existeUserName= Usuario.find_by_username(params["username"])
        if(existeMail==0 and existeUserName==0):  
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
            if(existeUserName!=0):
                mensaje="El nombre de usuario ingresado ya existe"
            flash(mensaje)
            return render_template("usuariosupdate.html",usuario=usuario_to_update)
    else:
        return render_template("usuariosupdate.html",usuario=usuario_to_update)


def delete(id):
    usuario_to_delete=Usuario.find_by_id(id)
    usuario_to_delete.activo=0
    db.session.commit()
    flash("El usuario se ha eliminado con exito")
    return redirect(url_for("usuario_index"))


    
    

        
      


        






