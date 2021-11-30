from re import I
from flask import jsonify, Blueprint, request
from app.models.recorrido import Recorrido
from app.models.configuracion import Configuracion


recorridos_evacuacion_api = Blueprint(
    "recorridos-evacuacion", __name__, url_prefix="/recorridos-evacuacion"
)


@recorridos_evacuacion_api.get("/")
def index():
    max_elementos = Configuracion.get_configs().maxElementos
    try:
        pagina = int(request.args.get("page", 1))
    except:
        pagina = 1
    recorridos_rows = Recorrido.query.paginate(
        page=pagina, per_page=max_elementos, error_out=False
    )
    data = {
        "recorridos": [recorrido.as_dict() for recorrido in recorridos_rows.items],
        "page": recorridos_rows.page,
        "total": recorridos_rows.pages,
    }
    return jsonify(data), 200
