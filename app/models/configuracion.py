from app.db import db
from sqlalchemy import Column,Integer,String



class Configuracion(db.Model):
    __tablename__="Configuracion"
    id=Column(Integer,primary_key=True)
    color1Privada=Column(String(255))
    color2Privada=Column(String(255))
    color3Privada=Column(String(255))
    color1Publica=Column(String(50))
    color2Publica=Column(String(50))
    color3Publica=Column(String(50))
    maxElementos=Column(Integer)
    criterio_orden=Column(String(50))
    sitio_en_mantenimiento=Column(Integer)
    

    @classmethod
    def getConfigs(csl):
        return  csl.query.all()[0]


    def __init__(self,color1Privada=None,color2Privada=None,color3Privada=None,color1Publica=None,color2Publica=None,color3Publica=None,maxElementos=None,criterio_orden=None,sitio_en_mantenimiento=None):
        self.color1Privada=color1Privada
        self.color2Privada=color2Privada
        self.color3Privada=color3Privada
        self.color1Publica=color1Publica
        self.color2Publica=color2Publica
        self.color3Publica=color3Publica
        self.maxElementos=maxElementos
        self.criterio_orden=criterio_orden
        self.sitio_en_mantenimiento=sitio_en_mantenimiento