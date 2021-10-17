from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from app.models.usuario import Usuario


def login():
    return render_template("auth/login.html")


def authenticate():
    conn = connection()
    params = request.form
    email=params['email']
    password=params['password']
    user=Usuario.find_user_by_email(email)
    if user and user.verify_password(user,password):
        #sesion iniciada correctamente
        print("funciono")
        session["user"]=user.email
        session["id"]=user.id
        flash("la sesion se inicio correctamente")
        return redirect(url_for("home"))
    else:
        #mail o contraseña invalidos
        print("no funciono")
        flash("usuario o clave incorrectos")
        return redirect(url_for("auth_login"))
       
    

    


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))