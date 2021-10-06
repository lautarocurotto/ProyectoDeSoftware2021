from app.db import db
from sqlalchemy import Column, Integer, String, Boolean

class Configuracion(db.Model):

    __tablename__ = "configuracion"
    id = Column(Integer, primary_key=True)
    color1Privada = Column(String(255), unique=False, nullable=True)
    color2Privada = Column(String(255), unique=False, nullable=True)
    color3Privada = Column(String(255), unique=False, nullable=True)
    color1Publica = Column(String(50), unique=False, nullable=True)
    color2Publica = Column(String(50), unique=False, nullable=True)
    color3Publica = Column(String(50), unique=False, nullable=True)
    maxElementos = Column(Integer)
    criterio_orden = Column(String(50), unique=False, nullable=False)
    sitio_en_mantenimiento = Column(Boolean)

    def __init__(self, color1Privada=None, color2Privada=None, color3Privada=None, color1Publica=None, color2Publica=None, color3Publica=None, maxElementos=5, criterio_orden=None, sitio_en_mantenimiento=False):
        self.color1Privada = color1Privada
        self.color2Privada = color2Privada
        self.color3Privada= color3Privada
        self.color1Publica = color1Publica
        self.color2Publica = color2Publica
        self.color3Publica = color3Publica
        self.maxElementos = maxElementos
        self.criterio_orden = criterio_orden
        self.sitio_en_mantenimiento = sitio_en_mantenimiento