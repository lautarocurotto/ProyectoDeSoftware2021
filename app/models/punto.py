from app.db import db
from sqlalchemy import Column,Integer,String,exists





class Punto(db.Model):
    __tablename__="Punto_encuentro"
    id=Column(Integer,primary_key=True)
    nombre=Column(String(255),unique=True)
    direccion=Column(String(255),unique=True)
    coordenadas=Column(String(255),unique=True)
    estado=Column(String(255),unique=True)
    telefono=Column(String(255),unique=True)
    email=Column(String(255),unique=True)

    @classmethod
    def dame_todo(csl,conf,nombree,estadoo, page):
        query=csl.query
        if conf.criterio_orden == "Alfabetico":
            query=query.order_by(csl.nombre)
        if nombree!=None:
                query=query.filter_by(nombre=nombree)
        if estadoo!=None:
                query=query.filter_by(estado=estadoo)
                
        return  query.limit(conf.maxElementos).offset(page*conf.maxElementos)
    
    @classmethod
    def existe_punto(cls,nombree):
        return cls.query.filter_by(nombre=nombree).count()
        

           

    def __init__(self,nombre=None,direccion=None,coordenadas=None,estado=None,telefono=None,email=None):
        self.nombre=nombre
        self.direccion=direccion
        self.coordenadas=coordenadas
        self.estado=estado
        self.telefono=telefono
        self.email=email