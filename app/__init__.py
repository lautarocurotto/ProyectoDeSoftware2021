from datetime import datetime
from os import environ
from flask import Flask, render_template,redirect,url_for,request, session, Blueprint ,abort
from config import config
from app import db
from app.db import db
from app.models.usuario import Usuario
from app.models.usuario_publico import Usuario_publico
from app.resources import punto
from app.resources import usuariospublicos
from app.resources import recorrido
from app.resources import configuracion
from app.resources import usuario
from app.resources import zonas
from flask_session import Session
from app.resources import auth
from app.helpers import handler
from app.helpers import auth as helper_auth
from app.helpers.auth import authenticated, check_permission
from app.resources.api.zonainundable_api import zonainundable_api
from app.resources import denuncia
from app.resources.api.denuncia import denuncia_api
from app.resources.api.puntos import puntos_encuentro_api
from flask_cors import CORS
from authlib.integrations.flask_client import OAuth

from app.resources.api.recorridos import recorridos_evacuacion_api

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)
    CORS(app)

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
    app.jinja_env.globals.update(cantidad_puntos=zonas.cantidad_puntos)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )


    # Usuarios publicos

    app.add_url_rule("/usuariospublicos","usuariopublico_index",usuariospublicos.index, methods=["POST", "GET"] )
    app.add_url_rule("/usuariospublicos/activar/<int:id>","usuariopublico_activar",usuariospublicos.activar,methods=["POST", "GET"] )
    # Rutas de Consultas
    
    app.add_url_rule("/usuarios","usuario_index",usuario.index, methods=["POST", "GET"] )
    app.add_url_rule("/usuarios/nuevo","usuario_create",usuario.create, methods=["POST"] )
    app.add_url_rule("/usuarios/update/<int:id>","usuario_update",usuario.update, methods=["POST", "GET"] )
    app.add_url_rule("/usuarios/delete/<int:id>","usuario_delete",usuario.delete)
    app.add_url_rule("/usuarios/activar/<int:id>","usuario_activar",usuario.activar)
    app.add_url_rule("/usuarios/show/<int:id>","usuario_show",usuario.show)
    app.add_url_rule("/usuarios/perfil","usuario_perfil",usuario.verPerfil)
    app.add_url_rule("/usuarios/perfilUpdate/<int:id>","usuario_update_perfil",usuario.updatePerfil, methods=["POST", "GET"] )
    app.add_url_rule("/usuarios/passwordUpdate/<int:id>","usuario_update_password",usuario.updatePassword, methods=["POST", "GET"] )

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
    app.add_url_rule("/denuncia/delete", "denuncia_delete", denuncia.delete_denuncia, methods=["POST"])
    # muchos setters de denuncia
    app.add_url_rule("/denuncia/set_coordenadas", "denuncia_set_coordenadas", denuncia.set_coordenadas, methods=["POST"])
    app.add_url_rule("/denuncia/set_descripcion", "denuncia_set_descripcion", denuncia.set_descripcion, methods=["POST"])
    app.add_url_rule("/denuncia/set_denunciante", "denuncia_set_denunciante", denuncia.set_denunciante, methods=["POST"])
    app.add_url_rule("/denuncia/set_categoria", "denuncia_set_categoria", denuncia.set_categoria, methods=["POST"])
    

    app.add_url_rule("/zonas","zonas_index",zonas.index,methods=["POST", "GET"])
    app.add_url_rule("/zonas/show/<int:id>","zonas_show",zonas.show)
    app.add_url_rule("/zonas/delete/<int:id>","zonas_delete",zonas.delete)
    app.add_url_rule("/zonas/activar/<int:id>","zonas_activar",zonas.activar)
    app.add_url_rule("/zonas/importar","zonas_importar",zonas.importar, methods=["POST","GET"] )
    app.add_url_rule("/zonas/eliminar/<int:id>","zonas_eliminar",zonas.delete_fisico)



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
    api.register_blueprint(zonainundable_api)
    api.register_blueprint(puntos_encuentro_api)
    api.register_blueprint(recorridos_evacuacion_api)
    app.register_blueprint(api)

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    app.register_error_handler(403, handler.forbidden_error)
    # Implementar lo mismo para el error 500    
    
    oauth = OAuth(app)
    google = oauth.register(
    name='google',
    client_id='468072504237-kimf5mfo7p6jmuu2ml0rqdm808cbthrf.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
    )

 

    @app.route('/logingoogle')
    def login():
        google = oauth.create_client('google')  # create the google oauth client
        redirect_uri = url_for('authorize', _external=True)
        return google.authorize_redirect(redirect_uri)


    @app.route('/authorize')
    def authorize():
        google = oauth.create_client('google')  # create the google oauth client
        token = google.authorize_access_token()  # Access token from google (needed to get user info)
        resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
        user_info = resp.json()
        user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
        # Here you use the profile/user data that you got and query your database find/register the user
        # and set ur own data in the session not the profile from google
        email=user.email
        name=user.given_name
        lastname=user.family_name
        session['profile']=user_info
        session.permanent=True
        session['user']=email
        session['id']=0
        print("se cargo el usuario")
        if(Usuario.find_by_email(email)!=0):
            #Ya esta concecido se loguea normal
            print('se logueo')
            usuario=Usuario.find_user_by_email(email)
            session['id']=usuario.id
            return redirect(url_for("home"))
        else:
            if(Usuario_publico.find_by_email(email)!=0):
                #Se loguea y se lo lleva a la pagina de inicio
                return redirect(url_for("home"))
                
            else:
                new_usuario=Usuario_publico(email=email,first_name=name,last_name=lastname,updated_at=datetime.now())
                db.session.add(new_usuario)
                db.session.commit()
                #Se carga el user en la bbdd y se lo lleva a la pagina de inicio
                return redirect(url_for("home"))
        
    return app