from app.db import db
from sqlalchemy import Column,Integer,String,exists
from sqlalchemy.orm import relationship
from app.models.coordenadas import Coordenadas

class Zonas(db.Model):
    __tablename__="Zonas"
    id=Column(Integer,primary_key=True)
    codigo=Column(String(255),unique=True)
    nombre=Column(String(255))
    estado=Column(String(255))
    color=Column(String(255))
    puntos=relationship(Coordenadas,cascade="all, delete")



    @classmethod
    def dame_todo(csl,conf,nombree,estadoo):
        query=csl.query
        if conf.criterio_orden == "Alfabetico":
            query=query.order_by(csl.nombre)
        if nombree!=None:
                query=query.filter_by(nombre=nombree)
        if estadoo!=None:
                query=query.filter_by(estado=estadoo)
                
        return query
    
    @classmethod
    def find_by_id(cls,id1):
        return cls.query.filter_by(id=id1).one()
    
    @classmethod
    def existe_zona(cls, nombre):
        return cls.query.filter_by(nombre=nombre).count() > 0
    
    @classmethod
    def get_by_name(cls,nombre):
        return cls.query.filter_by(nombre=nombre).one()

    @classmethod
    def cant_puntos(cls,id):
        return Coordenadas.query.filter_by(zonas_id=id).count()

    @classmethod
    def find_by_id_first(cls,e):
        return cls.query.filter_by(id=e).first()

    def as_dict(self):
        return {"id": self.id,
                "nombre":self.nombre,
                "coordenadas":[punto.as_dict() for punto in self.puntos],
                "color":self.color}
