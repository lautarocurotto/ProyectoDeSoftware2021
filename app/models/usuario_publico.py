from app.db import db
from sqlalchemy import Column,Integer,String,Boolean,DateTime,exists

class Usuario_publico(db.Model):
    __tablename__="Usuariopublico"
    id=Column(Integer,primary_key=True)
    email=Column(String(255),unique=True)
    first_name=Column(String(255))
    last_name=Column(String(255))
    updated_at=Column(DateTime)

    @classmethod
    def find_by_email(cls,mail):
        return cls.query.filter_by(email=mail).count()

    @classmethod
    def find_by_id(cls,id1):
        return cls.query.filter_by(id=id1).one()

    
    @classmethod
    def dame_todo(csl,conf,page):
        query=csl.query
        if conf.criterio_orden == "Alfabetico":
            query=query.order_by(csl.first_name)
        return query


    def __init__(self,email=None,first_name=None,last_name=None,updated_at=None):
        self.email=email
        self.first_name=first_name
        self.last_name=last_name
        self.updated_at=updated_at