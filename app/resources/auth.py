from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from app.models.usuario import Usuario
from app.helpers.auth import authenticated

def login():
    user = authenticated(session)
    if (not user):
        return render_template("auth/login.html")
    else:
        return redirect(url_for("home"))

def authenticate():
    conn = connection()
    params = request.form

    user = Usuario.find_by_email_and_pass(conn, params["email"], params["password"])

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))

    session["user"] = user.email
    session["id"] = user.id
    flash("La sesión se inició correctamente.")

    return redirect(url_for("home"))


def logout():
    user = authenticated(session)
    if (not user):
        abort(401)
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))