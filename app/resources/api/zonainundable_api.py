from flask import jsonify, Blueprint,request
from sqlalchemy.sql.expression import false
#from app.models.zonas import Zonas
from app.models.usuario import Usuario
from app.models.configuracion import Configuracion


zonainundable_api= Blueprint("consultas", __name__, url_prefix="/consultas")

@zonainundable_api.get("/<int:id>")
def index(id):
    if(id!=None):
        usuario_rows=Usuario.find_by_id_first(id)
        print(usuario_rows)
        if(usuario_rows):
            usuarios=usuario_rows.as_dict()
            return jsonify(Usuarios=usuarios)
        else:
            return "El ID del usuario pasado por parametro no existe en la base de datos"
    else:
        return "No se ha pasado el id"

@zonainundable_api.get("/")
def index2():
    pagee=int(request.args.get("page",1))
    
    usuario_rows=Usuario.query.paginate(page=pagee,per_page=2)
    print(usuario_rows)
    return {
        "usuarios":[item.as_dict() for item in usuario_rows.items],
        "page":usuario_rows.page,
        "total":usuario_rows.total,
    }


