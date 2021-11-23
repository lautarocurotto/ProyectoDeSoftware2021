from re import I
from flask import jsonify, Blueprint,request
from app.models.punto import Punto
from app.models.configuracion import Configuracion


puntos_encuentro_api= Blueprint("puntos-encuentro", __name__, url_prefix="/puntos-encuentro")


@puntos_encuentro_api.get("/")
def index():
    max_elementos=Configuracion.get_configs().maxElementos
    pagina=int(request.args.get("page",1))
    puntos_aux=Punto.query.paginate(page=1,per_page=max_elementos)
    if(Punto.cantidad_puntos()==0):
        data={"mensaje":"No hay puntos de encuentro en el sistema"}
        return jsonify(data),404
    if(pagina<=puntos_aux.pages):
        puntos_rows=Punto.query.paginate(page=pagina,per_page=max_elementos)
        data= {
            "puntos_encuentro":[punto.as_dict() for punto in puntos_rows.items],
            "page":puntos_rows.page,
            "total":puntos_rows.total,
        }
        return jsonify(data),200
    else:
        data={"mensaje":"Mandaste mal el numero de pagina"}
        return jsonify(data),400