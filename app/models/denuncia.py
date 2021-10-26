from app.db import db
from sqlalchemy import Column,Integer,String, DateTime, text

class Denuncia(db.Model):

    __tablename__ = "denuncia"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    category_id = Column(Integer)
    created_at = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    closed_at = Column(DateTime)
    description = Column(String)

    coordenates = Column(String) # No deberían ser un conjunto de puntos? Lats & alts ?

    status = Column(String, server_default=text('UNCONFIRMED'))
    operator_id = Column(Integer)
    denunciante_name = Column(String)
    denunciante_last_name = Column(String)
    denunciante_phone = Column(String)
    denunciante_email = Column(String)

    seguimiento = Column(String)

    @classmethod
    def get_all(cls, query_args):

        query = cls.query

        if(query_args.get("query-title") != None and query_args.get("query-title") != ''):
            print("Se filtro titutlo")
            query = query.filter(cls.title.like("%" + query_args.get("query-title") + "%"))

        if(query_args.get("query-status") != None and query_args.get("query-status") != ''):
            print("Se filtro status")
            query = query.filter_by(status = query_args.get("query-status"))
        
        if(query_args.get("query-datefrom") != None and query_args.get("query-datefrom") != ''):
            # print("query-datefrom: " + cls.created_at)
            query = query.filter(cls.created_at >= query_args.get("query-datefrom"))

        if(query_args.get("query-dateuntil") != None and query_args.get("query-dateuntil") != ''):
            query = query.filter(cls.created_at <= query_args.get("query-dateuntil"))

        return query

            