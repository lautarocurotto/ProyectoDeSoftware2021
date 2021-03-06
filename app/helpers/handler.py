from flask import render_template


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que quiere acceder no existe",
    }
    return render_template("error.html", **kwargs), 404


def unauthorized_error(e):
    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "No está autorizado para acceder a la url",
    }
    return render_template("error.html", **kwargs), 401


def forbidden_error(e):
    kwargs = {
        "error_name": "403 Forbidden Error",
        "error_description": "Se ha denegado su solicitud",
    }
    return render_template("error.html", **kwargs), 403
