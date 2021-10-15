from app.models.usuario import Usuario

def authenticated(session):
    return session.get("user")

def check_permission(user_id, permission):
    return Usuario.has_permission(user_id,permission)