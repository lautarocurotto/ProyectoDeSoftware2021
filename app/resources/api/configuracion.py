from flask import Blueprint, jsonify
from app.models.configuracion import Configuracion
import json

configuracion_api = Blueprint("configuracion", __name__, url_prefix="/configuracion")

@configuracion_api.get("/get-configs")
def get_configs():
    return jsonify(Configuracion.get_configs().as_dict()), 200