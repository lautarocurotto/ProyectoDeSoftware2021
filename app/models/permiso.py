from re import A
from sqlalchemy.sql.sqltypes import Date
from app.db import db
from sqlalchemy import Column,Integer,String,Boolean,DateTime,exists

class Permiso(db.Model):
    __tablename__="Permiso"
    id=Column(Integer,primary_key=True)
    nombre=Column(String(255),unique=True)

def __init__(self,id=None,nombre=None):
        self.id=id
        self.nombre=nombre
