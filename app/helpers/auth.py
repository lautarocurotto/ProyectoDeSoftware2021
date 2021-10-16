from app.models.usuario_tiene_rol import usuario_tiene_rol
from app.models.permiso import Permiso

def authenticated(session):
    return session.get("user")

def isAdmin(anID):
    return usuario_tiene_rol.find_by_id(anID) > 0

def hasPermission(aPermission, aUserID):
    return Permiso.has_permission(aPermission, aUserID) 