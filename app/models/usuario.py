from re import A
from sqlalchemy.sql.sqltypes import Date
from app.db import db
from sqlalchemy import Column,Integer,String,Boolean,DateTime,exists

class Usuario(db.Model):
    __tablename__="Usuario"
    id=Column(Integer,primary_key=True)
    email=Column(String(255),unique=True)
    username=Column(String(255),unique=True)
    password=Column(String(255),unique=True)
    activo=Column(Boolean,unique=True)
    updated_at=Column(DateTime,unique=True)
    created_at=Column(DateTime,unique=True)
    first_name=Column(String(255),unique=True)
    last_name=Column(String(255),unique=True)

    @classmethod
    def find_by_email(cls,mail):
        return cls.query.filter_by(email=mail).count()
    
    @classmethod
    def find_by_username(cls,usern):
        return cls.query.filter_by(username=usern).count()

    @classmethod
    def find_by_id(cls,id1):
        return cls.query.filter_by(id=id1).one()

    @classmethod
    def dame_todo(csl,activoo):
        query=csl.query
        if activoo!=None:
            query=query.filter_by(activo=1)
        else:
            query=query.all()
        return  query

    

        


    def __init__(self,email=None,username=None,password=None,activo=None,updated_at=None,created_at=None,first_name=None,last_name=None):
        self.email=email
        self.username=username
        self.password=password
        self.activo=activo
        self.updated_at=updated_at
        self.created_at=created_at
        self.first_name=first_name
        self.last_name=last_name
        