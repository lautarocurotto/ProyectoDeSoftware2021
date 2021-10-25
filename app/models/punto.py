from app.db import db
from sqlalchemy import Column,Integer,String,exists


class Punto(db.Model):
    __tablename__="Punto_encuentro"
    id=Column(Integer,primary_key=True)
    nombre=Column(String(255),unique=True)
    direccion=Column(String(255),unique=True)
    lat=Column(String(255),unique=True)
    lng=Column(String(255),unique=True)
    estado=Column(String(255),unique=True)
    telefono=Column(String(255),unique=True)
    email=Column(String(255),unique=True)

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
    def existe_punto(cls,nombree, idPunto=None,noContarMismoNombre=False):
        if noContarMismoNombre:
            return cls.query.filter(cls.nombre==nombree,cls.id !=idPunto).count()
        else:
            return cls.query.filter_by(nombre=nombree).count()
