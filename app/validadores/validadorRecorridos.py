
class ValidarForm():

    @classmethod
    def validar(nombree,descripcionn,estadoo,coordendas):
        print(nombree)
        print(descripcionn)
        print(estadoo)
        print("----------------------")
        print(nombree == "")
        print(descripcionn == "")
        print(estadoo == "")
        print(len(coordendas) < 3)
        if nombree == "":
            mensaje = "Falta el nombre del recorrido"
            print(mensaje)
            return mensaje
        if descripcionn == "":
            mensaje = "Falta la descripcion del recorrido"
            print(mensaje)
            return mensaje
        if estadoo == "":
            mensaje = "Falta el estado del recorrido"
            print(mensaje)
            return mensaje
        if len(coordendas) < 3:
            mensaje = "El recorrido debe tener al menos 3 puntos"
            print(mensaje)
            return mensaje
        return "Todo ok"