from app.db import db
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from app.models.coordenadas import Coordenadas

class Recorrido(db.Model):
    __tablename__="Recorrido"
    id=Column(Integer,primary_key=True)
    nombre=Column(String(255),unique=True)
    descripcion=Column(String(255))
    estado=Column(String(255))
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
    def existe_recorrido(cls,nombree, idReco=None,noContarMismoNombre=False):
        if noContarMismoNombre:
            return cls.query.filter(cls.nombre==nombree,cls.id !=idReco).count()
        else:
            return cls.query.filter_by(nombre=nombree).count()