from app.models.usuario import Usuario
from app.models.usuario_tiene_rol import usuario_tiene_rol



def authenticated(session):
    return session.get("user")


def check_permission(user_id, permission):
    return Usuario.has_permission(user_id, permission)


def isAdmin(anID):
    return usuario_tiene_rol.find_by_id(anID) > 0
