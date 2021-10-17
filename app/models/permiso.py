from re import A
from sqlalchemy.sql.sqltypes import Date
from app.db import db
<<<<<<< HEAD
from sqlalchemy import Column,Integer,String,Boolean,DateTime,exists

=======
from sqlalchemy import Column,Integer,String

from app.models.usuario_tiene_rol import usuario_tiene_rol
from app.models.usuario import Usuario
from app.models.rol_tiene_permiso import rol_tiene_permiso
>>>>>>> 7e6fa4e3dc0677d902e6c0d0879391d37eb95de2

class Permiso(db.Model):
    __tablename__="Permiso"
    id=Column(Integer,primary_key=True)
    nombre=Column(String,unique=True)

<<<<<<< HEAD
def __init__(self,id=None,nombre=None):
        self.id=id
        self.nombre=nombre
=======

    @classmethod
    def has_permission(cls, aPermission, aUserID):
        consulta = cls.query.join(
                rol_tiene_permiso, rol_tiene_permiso.permiso_id == Permiso.id
            ).join(
                usuario_tiene_rol, usuario_tiene_rol.rol_id == rol_tiene_permiso.rol_id
            ).join(
                Usuario, Usuario.id == usuario_tiene_rol.usuario_id
            ).filter(
                Usuario.id == aUserID
            ).filter(Permiso.nombre == aPermission)

        return consulta.count() > 0
>>>>>>> 7e6fa4e3dc0677d902e6c0d0879391d37eb95de2
