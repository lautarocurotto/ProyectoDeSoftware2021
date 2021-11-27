from re import I
from flask import jsonify, Blueprint,request
from app.models.punto import Punto
from app.models.configuracion import Configuracion


puntos_encuentro_api= Blueprint("puntos-encuentroo", __name__, url_prefix="/puntos-encuentro")


@puntos_encuentro_api.get("/")
def index():
    max_elementos=Configuracion.get_configs().maxElementos
    try:
        pagina=int(request.args.get("page",1))
    except:
        pagina=1
    puntos_rows=Punto.query.paginate(page=pagina,per_page=max_elementos,error_out=False)
    data= {
            "puntos_encuentro":[punto.as_dict() for punto in puntos_rows.items],
            "page":puntos_rows.page,
            "total":puntos_rows.total,
        }
    return jsonify(data),200
   