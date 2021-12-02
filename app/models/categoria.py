from sqlalchemy.orm import relationship
from app.db import db
from sqlalchemy import Column, Integer, String


class Categoria(db.Model):

    __tablename__ = "denuncia_categoria"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    denuncias = relationship("Denuncia", backref="categoria")
