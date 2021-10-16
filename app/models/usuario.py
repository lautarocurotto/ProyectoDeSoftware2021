from re import A
from sqlalchemy.sql.expression import select
from sqlalchemy.sql.sqltypes import Date
from app.db import db
from sqlalchemy import Column,Integer,String,Boolean,DateTime,exists
from app.models import usuario_tiene_rol
from sqlalchemy import Column,Integer,String,Boolean,DateTime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app.models.permiso import Permiso 
from app.models.rol_tiene_permiso import rol_tiene_permiso
from app.models.usuario_tiene_rol import usuario_tiene_rol
from app.models.roles import Rol

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
    def create_password(cls,password):
        return generate_password_hash(password)

    @classmethod
    def verify_password(cls,password):
        return check_password_hash(cls.password,password)
    

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
    def existe_mail(cls,nombree,idPunto=None):
            return cls.query.filter(cls.email==nombree,cls.id !=idPunto).count()
    
    @classmethod
    def existe_username(cls,nombre,idPunto=None):
            return cls.query.filter(cls.username==nombre,cls.id !=idPunto).count()
    
    @classmethod
    def find_user_by_email(cls,e):
        return cls.query.filter_by(email=e).one()




    @classmethod
    def dame_todo(csl,conf,page,activoo,nombre):
        query=csl.query
        if conf.criterio_orden == "Alfabetico":
            query=query.order_by(csl.username)
        if nombre!=None:
            query=query.filter_by(username=nombre)
        if activoo!=None:
            if activoo=='activo':
                query=query.filter_by(activo=1)
            if activoo=='bloqueado':
                query=query.filter_by(activo=0)

        return query.limit(conf.maxElementos).offset(page*conf.maxElementos)

    
    @classmethod
    def find_by_email_and_pass(cls,conn, email, password):
      return cls.query.filter_by(email=email,password=password).first()   

    @classmethod
    def has_permission(cls, aUserID, aPermission):
        consulta=cls.query.join(usuario_tiene_rol, usuario_tiene_rol.usuario_id == Usuario.id).join(rol_tiene_permiso, usuario_tiene_rol.rol_id == rol_tiene_permiso.rol_id).join(Permiso, rol_tiene_permiso.permiso_id == Permiso.id).filter(Usuario.id==aUserID).filter(Permiso.nombre == aPermission)
        return (consulta.count() > 0)

    def __init__(self,email=None,username=None,password=None,activo=None,updated_at=None,created_at=None,first_name=None,last_name=None):
        self.email=email
        self.username=username
        self.password=self.create_password(password)
        self.activo=activo
        self.updated_at=updated_at
        self.created_at=created_at
        self.first_name=first_name
        self.last_name=last_name
        