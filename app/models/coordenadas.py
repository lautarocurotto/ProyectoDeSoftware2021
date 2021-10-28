from app.db import db
from sqlalchemy import Column,Integer,String,ForeignKey

class Coordenadas(db.Model):
    __tablename__="Coordenadas"
    id=Column(Integer,primary_key=True)
    lat=Column(String(255))
    lng=Column(String(255))

    recorrido_id=Column(Integer,ForeignKey('Recorrido.id'))


    def __init__(self,lati=None,lngg=None):
        self.lat=lati
        self.lng=lngg
        