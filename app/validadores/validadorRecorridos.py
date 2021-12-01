
class ValidarForm():

    @classmethod
    def validar(cls,nombree,descripcionn,estadoo,coordendas):
        if nombree == "":
            mensaje = "Falta el nombre del recorrido"
            return mensaje
        if descripcionn == "":
            mensaje = "Falta la descripcion del recorrido"
            return mensaje
        if estadoo == "":
            mensaje = "Falta el estado del recorrido"
            return mensaje
        if len(coordendas) < 3:
            mensaje = "El recorrido debe tener al menos 3 puntos"
            return mensaje
        return "Todo ok"