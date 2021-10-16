from re import A
from sqlalchemy.sql.sqltypes import Date
from app.db import db
from sqlalchemy import Column,Integer,String

from app.models.usuario_tiene_rol import usuario_tiene_rol
from app.models.usuario import Usuario
from app.models.rol_tiene_permiso import rol_tiene_permiso

class Permiso(db.Model):
    __tablename__="Permiso"
    id=Column(Integer,primary_key=True)
    nombre=Column(String,unique=True)


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