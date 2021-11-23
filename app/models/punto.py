from app.db import db
from sqlalchemy import Column,Integer,String,exists


class Punto(db.Model):
    __tablename__="Punto_encuentro"
    id=Column(Integer,primary_key=True)
    nombre=Column(String(255),unique=True)
    direccion=Column(String(255))
    lat=Column(String(255))
    lng=Column(String(255))
    estado=Column(String(255))
    telefono=Column(String(255))
    email=Column(String(255))

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
    
    def as_dict(self):
        return {"id": self.id,
                "nombre":self.nombre,
                "direccion":self.direccion,
                "lat":self.lat,
                "long":self.lng,
                "telefono":self.telefono,
                "email":self.email}

    @classmethod
    def cantidad_puntos(cls):
            return cls.query.count()
        