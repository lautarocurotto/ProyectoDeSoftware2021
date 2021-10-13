from re import A
from sqlalchemy.sql.sqltypes import Date
from app.db import db
from sqlalchemy import Column,Integer,String,Boolean,DateTime,exists


class usuario_tiene_rol(db.Model):
    __tablename__="usuario_tiene_rol"
    usuario_id=Column(Integer,primary_key=True)
    rol_id=Column(Integer,primary_key=True)

    @classmethod
    def find_by_id(cls,id1):
        return cls.query.filter_by(usuario_id=id1).count()

    


def __init__(self,usuario_id=None,rol_id=None):
        self.usuario_id=usuario_id
        self.rol_id=rol_id


