from flask import Blueprint, request
from werkzeug.wrappers import response
from app.db import db
from email_validator import validate_email, EmailNotValidError
from app.models.denuncia import Denuncia
from app.models.categoria import Categoria

denuncia_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")

@denuncia_api.post("")
def new_denuncia():
    """Método para usar en la API"""
    postdata = request.get_json()

    try:
        validate_email(postdata["email_denunciante"])
    except EmailNotValidError:
        return response.Response(status=500)

    try:
        int(postdata["categoria_id"])
    except:
        return response.Response(status=500)
    
    Categoria.query.get_or_404(postdata["categoria_id"])

    if postdata["coordenadas"] == '':
        return response.Response(status=500)

    if postdata["apellido_denunciante"] == '':
        return response.Response(status=500)

    if postdata["nombre_denunciante"] == '':
        return response.Response(status=500)

    if postdata["telcel_denunciante"] == '':
        return response.Response(status=500)

    if postdata["titulo"] == '':
        return response.Response(status=500)

    if postdata["descripcion"] == '':
        return response.Response(status=500)

    db.session.add(
        Denuncia(
            category_id = postdata["categoria_id"],
            coordenates = postdata["coordenadas"],
            denunciante_name = postdata["nombre_denunciante"],
            denunciante_last_name = postdata["apellido_denunciante"],
            denunciante_phone = postdata["telcel_denunciante"],
            denunciante_email = postdata["email_denunciante"],
            title = postdata["titulo"],
            description = postdata["descripcion"]
        ))

    try:
        db.session.commit()
    except Exception as e:
        return (str(e))
        
    return response.Response(status=201)