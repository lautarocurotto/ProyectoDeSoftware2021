from sqlalchemy.orm import backref, relationship
from app.db import db
from sqlalchemy import Column,Integer,String, DateTime, text

class Categoria(db.Model):

    __tablename__ = "denuncia_categoria"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    denuncias = relationship('Denuncia', backref="categoria")

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def as_dict(self):
        return {
            "id" : self.id,
            "name" : self.name
        }


