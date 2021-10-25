from app.db import db
from sqlalchemy import Column,Integer,String, DateTime

class Denuncia(db.Model):

    __tablename__ = "denuncia"
    id = Column(Integer, primary_key = True)
    title = Column(String)
    category_id = Column(Integer)
    created_at = Column(DateTime)
    closed_at = Column(DateTime)
    description = Column(String)

    coordenates = Column(String) # No deberían ser un conjunto de puntos? Lats & alts ?

    status = Column(String)
    operator_id = Column(Integer)
    denunciante_name = Column(String)
    denunciante_last_name = Column(String)
    denunciante_phone = Column(String)
    denunciante_email = Column(String)

    @classmethod
    def get_all(cls, query_args):

        query = cls.query

        if(query_args.get("query-title") != None and query_args.get("query-title") != ''):
            print("Se filtro titutlo")
            query = query.filter(cls.title.like("%" + query_args.get("query-title") + "%"))

        if(query_args.get("query-status") != None and query_args.get("query-status") != ''):
            print("Se filtro status")
            query = query.filter_by(status = query_args.get("query-status"))
        
        # if(query_args.get("query-datefrom") != None and query_args.get("query-datefrom") != ''):
        #     print("Se filtro por fecha from")
        #     cls.query.filter_by(DateTime(cls.created_at) > DateTime(query_args.get("query-datefrom")))

        # if(query_args.get("query-dateuntil") != None and query_args.get("query-dateuntil") != ''):
        #     cls.query.filter_by(created_at = query_args.get("query-dateuntil"))

        return query

            