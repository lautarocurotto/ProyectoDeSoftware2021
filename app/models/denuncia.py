from re import S
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import ForeignKey
from app.db import db
from sqlalchemy import Column,Integer,String, DateTime, text
from app.models.seguimiento import Seguimiento
from app.models.categoria import Categoria
from app.models.usuario import Usuario

class Denuncia(db.Model):

    __tablename__ = "denuncia"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    category_id = Column(Integer, ForeignKey('denuncia_categoria.id'))
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    closed_at = Column(DateTime)
    description = Column(String)

    coordenada_lat = Column(String)
    coordenada_lng = Column(String)

    status = Column(String, server_default=text('UNCONFIRMED'))
    operator_id = Column(Integer)
    denunciante_name = Column(String)
    denunciante_last_name = Column(String)
    denunciante_phone = Column(String)
    denunciante_email = Column(String)

    seguimientos = relationship('Seguimiento', backref="denuncia")

    @classmethod
    def get_all(cls, query_args):

        query = cls.query

        if(query_args.get("query-title") != None and query_args.get("query-title") != ''):
            query = query.filter(cls.title.like("%" + query_args.get("query-title") + "%"))

        if(query_args.get("query-status") != None and query_args.get("query-status") != ''):
            query = query.filter_by(status = query_args.get("query-status"))
        
        if(query_args.get("query-datefrom") != None and query_args.get("query-datefrom") != ''):
            query = query.filter(cls.created_at >= query_args.get("query-datefrom"))

        if(query_args.get("query-dateuntil") != None and query_args.get("query-dateuntil") != ''):
            query = query.filter(cls.created_at <= query_args.get("query-dateuntil"))

        return query

            