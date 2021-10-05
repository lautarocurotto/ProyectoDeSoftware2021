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
    def dame_todo(csl,nombre,estado):
        #filtrar por cantidad max y orden#
        #filtrar por nombre y estado#


        return  csl.query.all()


    def __init__(self,nombre=None,direccion=None,coordenadas=None,estado=None,telefono=None,email=None):
        self.nombre=nombre
        self.direccion=direccion
        self.coordenadas=coordenadas
        self.estado=estado
        self.telefono=telefono
        self.email=email