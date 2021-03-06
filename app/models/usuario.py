from app.db import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from app.models import usuario_tiene_rol
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from sqlalchemy.orm import relationship
from app.models.usuario_tiene_rol import usuario_tiene_rol


class Usuario(db.Model):
    __tablename__ = "Usuario"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True)
    password = Column(String(255))
    activo = Column(Boolean)
    updated_at = Column(DateTime)
    created_at = Column(DateTime)
    first_name = Column(String(255))
    last_name = Column(String(255))
    roles = relationship(
        "Rol", secondary=usuario_tiene_rol.__tablename__, backref="usuarios"
    )

    seguimientos = relationship("Seguimiento", backref="author")

    @classmethod
    def verify_password(cls, user, password):
        query = check_password_hash(user.password, password)
        return query

    @classmethod
    def create_password(cls, password):
        return generate_password_hash(password)

    @classmethod
    def find_by_email(cls, mail):
        return cls.query.filter_by(email=mail).count()

    @classmethod
    def find_by_username(cls, usern):
        return cls.query.filter_by(username=usern).count()

    @classmethod
    def find_by_id(cls, id1):
        return cls.query.filter_by(id=id1).one()

    @classmethod
    def find_by_id_first(cls, id1):
        return cls.query.filter_by(id=id1).first()

    @classmethod
    def existe_mail(cls, nombree, idPunto=None):
        return cls.query.filter(cls.email == nombree, cls.id != idPunto).count()

    @classmethod
    def existe_username(cls, nombre, idPunto=None):
        return cls.query.filter(cls.username == nombre, cls.id != idPunto).count()

    @classmethod
    def find_user_by_email(cls, e):
        return cls.query.filter_by(email=e).one()

    @classmethod
    def find_user_by_email_first(cls, e):
        return cls.query.filter_by(email=e).first()

    @classmethod
    def dame_todo(csl, conf, page, activoo, nombre):
        query = csl.query
        if conf.criterio_orden == "Alfabetico":
            query = query.order_by(csl.username)
        if nombre != None:
            query = query.filter_by(username=nombre)
        if activoo != None:
            if activoo == "activo":
                query = query.filter_by(activo=1)
            if activoo == "bloqueado":
                query = query.filter_by(activo=0)

        return query

    @classmethod
    def find_by_email_and_pass(cls, conn, email, password):
        return cls.query.filter_by(email=email, password=password).first()

    @classmethod
    def has_permission(cls, aUserID, aPermission):
        usuario = Usuario.find_by_id_first(aUserID)
        lista = []
        for rol in usuario.roles:
            for permiso in rol.permisos:
                lista.append(permiso.nombre)
        if aPermission in lista:
            return True
        else:
            return False

    # consulta=cls.query.join(usuario_tiene_rol, usuario_tiene_rol.usuario_id == Usuario.id).join(rol_tiene_permiso, usuario_tiene_rol.rol_id == rol_tiene_permiso.rol_id).join(Permiso, rol_tiene_permiso.permiso_id == Permiso.id).filter(Usuario.id==aUserID).filter(Permiso.nombre == aPermission)
    #    return (consulta.count() > 0)

    def as_dict(self):
        #return {attr.name: getattr(self,attr.name) for attr in self.__table__.columns}
        return {"email": self.email,
                "username":self.username,
                "firstname":self.first_name}

    


    def __init__(self,email=None,username=None,password=None,activo=None,updated_at=None,created_at=None,first_name=None,last_name=None):
        self.email=email
        self.username=username
        if(password!=None):
            self.password=self.create_password(password)
        self.activo=activo
        self.updated_at=updated_at
        self.created_at=created_at
        self.first_name=first_name
        self.last_name=last_name
        
