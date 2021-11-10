from sqlalchemy.orm import backref, relationship
from app.db import db
from sqlalchemy import Column,Integer,String, DateTime, text

class Categoria(db.Model):

    __tablename__ = "denuncia_categoria"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    denuncias = relationship('Denuncia', backref="categoria")