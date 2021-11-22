from flask import jsonify, Blueprint,request
from app.models.punto import Punto
from app.models.configuracion import Configuracion


puntos_encuentro_api= Blueprint("puntos-encuentro", __name__, url_prefix="/puntos-encuentro")


@puntos_encuentro_api.get("/")
def index():
    pagee=int(request.args.get("page",1))
    per_page=Configuracion.get_configs().maxElementos
    puntos_rows=Punto.query.paginate(page=pagee,per_page=per_page)
    data= {
        "puntos_encuentro":[item.as_dict() for item in puntos_rows.items],
        "page":puntos_rows.page,
        "total":puntos_rows.total,
    }
    return jsonify(data),200