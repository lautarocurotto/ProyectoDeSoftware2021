from re import A
from sqlalchemy.sql.sqltypes import Date
from app.db import db
from sqlalchemy import Column,Integer,String,Boolean,DateTime,exists


class Rol(db.Model):
    __tablename__="Rol"
    id=Column(Integer,primary_key=True)
    nombre=Column(Integer,unique=True)


    


def __init__(self,id=None,nombre=None):
        self.id=id
        self.nombre=nombre


