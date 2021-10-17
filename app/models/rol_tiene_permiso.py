from re import A
from sqlalchemy.orm import load_only
from sqlalchemy.sql.sqltypes import Date
from app.db import db
from sqlalchemy import Column,Integer,String,Boolean,DateTime,exists


class rol_tiene_permiso(db.Model):
    __tablename__="rol_tiene_permiso"
    rol_id=Column(Integer,primary_key=True)
    permiso_id=Column(Integer,primary_key=True)


def __init__(self,rol_id=None,permiso_id=None):
        self.rol_id=rol_id
        self.permiso_id=permiso_id
