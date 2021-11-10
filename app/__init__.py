from os import environ
from flask import Flask, render_template,redirect,url_for,request, session, Blueprint
from config import config
from app import db
from app.resources import punto
from app.resources import recorrido
from app.resources import configuracion
from app.resources import usuario
from app.resources import zonas
from flask_session import Session
from app.resources import auth
from app.helpers import handler
from app.helpers import auth as helper_auth
from app.helpers.auth import authenticated, check_permission
from app.resources import denuncia
from app.resources.api.denuncia import denuncia_api


def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    

    # Configure db
    db.init_app(app)

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    # app.jinja_env.globals.update(isAdmin=helper_auth.isAdmin)
    app.jinja_env.globals.update(configs=configuracion.get_configs)
    app.jinja_env.globals.update(tiene_permiso=helper_auth.check_permission)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )

    # Rutas de Consultas
    
    app.add_url_rule("/usuarios","usuario_index",usuario.index, methods=["POST", "GET"] )
    app.add_url_rule("/usuarios/nuevo","usuario_create",usuario.create, methods=["POST"] )
    app.add_url_rule("/usuarios/update/<int:id>","usuario_update",usuario.update, methods=["POST", "GET"] )
    app.add_url_rule("/usuarios/delete/<int:id>","usuario_delete",usuario.delete)
    app.add_url_rule("/usuarios/activar/<int:id>","usuario_activar",usuario.activar)
    app.add_url_rule("/usuarios/show/<int:id>","usuario_show",usuario.show)
    app.add_url_rule("/usuarios/perfil","usuario_perfil",usuario.verPerfil)
    app.add_url_rule("/usuarios/perfilUpdate/<int:id>","usuario_update_perfil",usuario.updatePerfil, methods=["POST", "GET"] )


    app.add_url_rule("/puntos","puntos_index",punto.index,methods=["POST", "GET"])
    app.add_url_rule("/puntos/nuevo","puntos_create",punto.create, methods=["POST"] )
    app.add_url_rule("/puntos/update/<int:id>","puntos_update",punto.update, methods=["POST", "GET"] )
    app.add_url_rule("/puntos/delete/<int:id>","puntos_delete",punto.delete)
    app.add_url_rule("/puntos/show/<int:id>","puntos_show",punto.show)

    app.add_url_rule("/recorridos","recorridos_index",recorrido.index,methods=["POST", "GET"])
    app.add_url_rule("/recorridos/nuevo","recorridos_create",recorrido.create, methods=["POST"] )
    app.add_url_rule("/recorridos/update/<int:id>","recorridos_update",recorrido.update, methods=["GET"] )
    app.add_url_rule("/recorridos/updateCurrent","recorridos_updateCurrent",recorrido.updateCurrent, methods=["POST"] )
    app.add_url_rule("/recorridos/delete/<int:id>","recorridos_delete",recorrido.delete)
    app.add_url_rule("/recorridos/show/<int:id>","recorridos_show",recorrido.show)

    app.add_url_rule("/configuracion", "configuracion", configuracion.index)
    app.add_url_rule("/configuracion/set/mantenimiento", "config_toggle_mantenimiento", configuracion.toggleMaintenance)
    app.add_url_rule("/configuracion/set_configs", "set_configs", configuracion.set_configs,  methods=["POST"])


    app.add_url_rule("/denuncias", "denuncias", denuncia.index)
    app.add_url_rule("/denuncia/<int:id>", "denuncia_show", denuncia.show)
    app.add_url_rule("/denuncia/new", "denuncia_new", denuncia.new_denuncia, methods=["POST"])
    app.add_url_rule("/denuncia/set-status", "denuncia_set_status", denuncia.set_status, methods=["POST"])
    app.add_url_rule("/denuncia/update-seguimiento", "denuncia_update_seguimiento", denuncia.update_seguimiento, methods=["POST"])

    app.add_url_rule("/zonas","zonas_index",zonas.index,methods=["POST", "GET"])
    app.add_url_rule("/zonas/show/<int:id>","zonas_show",zonas.show)
    app.add_url_rule("/zonas/delete/<int:id>","zonas_delete",zonas.delete)
    app.add_url_rule("/zonas/activar/<int:id>","zonas_activar",zonas.activar)


    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        user = authenticated(session)
        if (not user):
            return redirect(url_for("auth_login"))
        else:
            return render_template("home.html")
    


    # Rutas de API-REST (usando Blueprints)

    api = Blueprint("api", __name__, url_prefix="/api")
    api.register_blueprint(denuncia_api)

    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(403, handler.forbidden_error)
    # Implementar lo mismo para el error 500    
    

    
    return app