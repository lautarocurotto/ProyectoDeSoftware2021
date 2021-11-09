from app.db import db
from sqlalchemy import Column,Integer,String,ForeignKey

class Coordenadas(db.Model):
    __tablename__="Coordenadas"
    id=Column(Integer,primary_key=True)
    lat=Column(String(255))
    lng=Column(String(255))
    tipo=Column(String(255))

    recorrido_id=Column(Integer,ForeignKey('Recorrido.id'))


    def __init__(self,lat=None,lng=None,tipo=None):
        self.lat=lat
        self.lng=lng
        self.tipo=tipo

    @classmethod
    def devolverPorCoordenadasRecorrido(cls,latitud,longitud):
        return cls.query.filter_by(lat=latitud,lng=longitud,tipo="recorrido").first()
        