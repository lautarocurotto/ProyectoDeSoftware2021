from flask import jsonify, Blueprint, request
from sqlalchemy.sql.expression import false
from app.models.zonas import Zonas
from app.models.usuario import Usuario
from app.models.configuracion import Configuracion


zonainundable_api = Blueprint("consultas", __name__, url_prefix="/consultas")


@zonainundable_api.get("/<int:id>")
def index(id):
    if id != None:
        zona_rows = Zonas.find_by_id_first(id)
        print(zona_rows)
        if zona_rows:
            usuarios = zona_rows.as_dict()
            return jsonify(Zonas=usuarios), 200
        else:
            return (
                "El ID de la zona  pasado por parametro no existe en la base de datos",
                400,
            )
    else:
        return 404


@zonainundable_api.get("/")
def index2():
    pagee = int(request.args.get("page", 1))
    per_page = Configuracion.get_configs().maxElementos
    zona_rows = Zonas.query.paginate(page=pagee, per_page=per_page)
    print(zona_rows)
    return {
        "zonas": [item.as_dict() for item in zona_rows.items],
        "page": zona_rows.page,
        "total": zona_rows.total,
    }, 200
