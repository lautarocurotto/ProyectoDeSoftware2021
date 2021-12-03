from app.db import db
from sqlalchemy import Column, Integer, String, ForeignKey


class Coordenadas(db.Model):
    __tablename__ = "Coordenadas"
    id = Column(Integer, primary_key=True)
    lat = Column(String(255))
    lng = Column(String(255))
    tipo = Column(String(255))

    recorrido_id = Column(Integer, ForeignKey("Recorrido.id"))
    zonas_id = Column(Integer, ForeignKey("Zonas.id"))

    def as_dict(self):
        return {"lat": self.lat, "lon": self.lng}

    def __init__(self, lat=None, lng=None, tipo=None):
        self.lat = lat
        self.lng = lng
        self.tipo = tipo

    def as_array(self):
        return [self.lat, self.lng]
