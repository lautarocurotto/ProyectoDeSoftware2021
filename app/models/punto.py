from app.db import db
from sqlalchemy import Column,Integer,String





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
    def dame_todo(csl,conf,nombree,estadoo):
        query=csl.query
        if conf.criterio_orden == "Alfabetico":
            print("Entre a ordenar por nombre")
            query=query.order_by(csl.nombre)
        if nombree!=None:
                print("Entre a filtrar por nombre")
                query=query.filter_by(nombre=nombree)
        if estadoo!=None:
                print("Entre a filtrar por estado")
                query=query.filter_by(estado=estadoo)
        return  query.limit(conf.maxElementos).all()
        

           

    def __init__(self,nombre=None,direccion=None,coordenadas=None,estado=None,telefono=None,email=None):
        self.nombre=nombre
        self.direccion=direccion
        self.coordenadas=coordenadas
        self.estado=estado
        self.telefono=telefono
        self.email=email