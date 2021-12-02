from flask import Blueprint, request, jsonify
from werkzeug.wrappers import response
from app.db import db
from email_validator import validate_email, EmailNotValidError
from app.models.denuncia import Denuncia
from app.models.categoria import Categoria
import json

denuncia_api = Blueprint("denuncias", __name__, url_prefix="/denuncias")


@denuncia_api.post("")
def new_denuncia():
    """Método para usar en la API"""
    postdata = request.get_json()
    

    try:
        validate_email(postdata["email_denunciante"])
    except EmailNotValidError:
        return response.Response(
            status=400,
            response=json.dumps({"error": "Email inváido"}),
            content_type="application/json",
        )

    try:
        int(postdata["categoria_id"])
    except:
        return response.Response(
            status=400,
            response=json.dumps({"error": "ID de categoría inválido."}),
            content_type="application/json",
        )

    if Categoria.find_by_id(postdata["categoria_id"]) == None:
        return response.Response(
            status=422,
            response=json.dumps({"error": "ID de categoría inexistente."}),
            content_type="application/json",
        )

    if postdata["coordenadas"] == "":
        return response.Response(
            status=400,
            response=jsonify(
                {
                    "error": 'Coordenadas vacías. Debe introducir coordenadas. Ej: "-57, 57".'
                }
            ),
            content_type="application/json",
        )

    if postdata["apellido_denunciante"] == "":
        return response.Response(
            status=400,
            response=json.dumps({"error": "Debe introducir un apellido."}),
            content_type="application/json",
        )

    if postdata["nombre_denunciante"] == "":
        return response.Response(
            status=400,
            response=json.dumps({"error": "Debe introducir un nombre."}),
            content_type="application/json",
        )

    if postdata["telcel_denunciante"] == "":
        return response.Response(
            status=400,
            response=json.dumps({"error": "Debe introducir un número de teléfono."}),
            content_type="application/json",
        )

    if postdata["titulo"] == "":
        data = {
            "error" : "Debe introducir un titulo"
        }
        return jsonify(data), 400

    if postdata["descripcion"] == "":
        return response.Response(
            status=400,
            response=json.dumps({"error": "Debe introducir una descripción."}),
            content_type="application/json",
        )

    coordenadas = postdata["coordenadas"].split(", ")

    db.session.add(
        Denuncia(
            category_id=postdata["categoria_id"],
            coordenada_lat=coordenadas[0],
            coordenada_lng=coordenadas[1],
            denunciante_name=postdata["nombre_denunciante"],
            denunciante_last_name=postdata["apellido_denunciante"],
            denunciante_phone=postdata["telcel_denunciante"],
            denunciante_email=postdata["email_denunciante"],
            title=postdata["titulo"],
            description=postdata["descripcion"],
        )
    )

    try:
        db.session.commit()
    except Exception as e:
        return str(e)

    atributos = {"atributos": postdata}

    return response.Response(
        status=201, response=json.dumps(atributos), content_type="application/json"
    )

@denuncia_api.get("/get-categorias")
def getCategorias():

    data = {
        "categorias" : [categoria.as_dict() for categoria in Categoria.query.all()]
    }
    
    return jsonify(data), 200