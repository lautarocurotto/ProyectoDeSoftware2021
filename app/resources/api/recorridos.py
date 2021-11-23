from re import I
from flask import jsonify, Blueprint,request
from app.models.recorrido import Recorrido
from app.models.configuracion import Configuracion


recorridos_evacuacion_api= Blueprint("puntos-encuentro", __name__, url_prefix="/recorridos-evacuacion")


@recorridos_evacuacion_api.get("/")
def index():
    max_elementos=Configuracion.get_configs().maxElementos
    pagina=int(request.args.get("page",1))
    recorridos_aux=Recorrido.query.paginate(page=1,per_page=max_elementos)
    if(Recorrido.cantidad_recorridos()==0):
        data={"mensaje":"No hay recorridos de evacuacion en el sistema"}
        return jsonify(data),404
    if(pagina<=recorridos_aux.pages):
        recorridos_rows=Recorrido.query.paginate(page=pagina,per_page=max_elementos)
        data= {
            "recorridos":[recorrido.as_dict() for recorrido in recorridos_rows.items],
            "page":recorridos_rows.page,
            "total":recorridos_rows.total,
        }
        return jsonify(data),200
    else:
        data={"mensaje":"Mandaste mal el numero de pagina"}
        return jsonify(data),400