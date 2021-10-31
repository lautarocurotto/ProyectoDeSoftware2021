from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date
from app.db import db
from sqlalchemy import Column,Integer,String, Date
from app.models.usuario import Usuario

class Seguimiento(db.Model):

    __tablename__ = "denuncia_seguimiento"
    id = Column(Integer, primary_key=True)
    denuncia_id = Column(Integer, ForeignKey('denuncia.id'))
    description = Column(String)
    author_id = Column(Integer, ForeignKey(Usuario.id))
    created_at = Column(Date)