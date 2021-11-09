from app.db import db
from sqlalchemy import Column,Integer,String,exists


class Zonas(db.Model):
    __tablename__="Zonas"
    id=Column(Integer,primary_key=True)
    codigo=Column(String(255),unique=True)
    nombre=Column(String(255))
    estado=Column(String(255))

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