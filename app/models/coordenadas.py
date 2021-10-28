from app.db import db
from sqlalchemy import Column,Integer,String,ForeignKey

class Coordenadas(db.Model):
    __tablename__="Coordenadas"
    id=Column(Integer,primary_key=True)
    lat=Column(String(255))
    lng=Column(String(255))

    recorrido_id=Column(Integer,ForeignKey('Recorrido.id'), nullable=True)
    
    
    @classmethod
    def getAll(csl):
        return  csl.query.all()


    def __init__(self,lat=None,lng=None):
        self.lat=lat
        self.lng=lng
        