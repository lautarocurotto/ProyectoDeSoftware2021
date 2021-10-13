from os import environ
from flask import Flask, render_template,redirect,url_for,request
from config import config
from app import db
from app.resources import punto
from app.resources import configuracion
from app.resources import usuario




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
    #app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(configs=configuracion.getConfigs)

    # Autenticación
    

    # Rutas de Consultas
    
    app.add_url_rule("/usuarios","usuario_index",usuario.index, methods=["POST", "GET"] )
    app.add_url_rule("/usuarios/nuevo","usuario_create",usuario.create, methods=["POST"] )
    app.add_url_rule("/usuarios/update/<int:id>","usuario_update",usuario.update, methods=["POST", "GET"] )
    app.add_url_rule("/usuarios/delete/<int:id>","usuario_delete",usuario.delete)

    app.add_url_rule("/puntos","puntos_index",punto.index,methods=["POST", "GET"])
    app.add_url_rule("/puntos/nuevo","puntos_create",punto.create, methods=["POST"] )
    app.add_url_rule("/puntos/update/<int:id>","puntos_update",punto.update, methods=["POST", "GET"] )
    app.add_url_rule("/puntos/delete/<int:id>","puntos_delete",punto.delete)
    app.add_url_rule("/puntos/show/<int:id>","puntos_show",punto.show)

    app.add_url_rule("/configuracion", "configuracion", configuracion.index)
    app.add_url_rule("/configuracion/set/color1", "config_set_color1", configuracion.setColor1, methods=["POST"])
    app.add_url_rule("/configuracion/set/color2", "config_set_color2", configuracion.setColor2, methods=["POST"])
    app.add_url_rule("/configuracion/set/color3", "config_set_color3", configuracion.setColor3, methods=["POST"])
    app.add_url_rule("/configuracion/set/criterio", "config_set_criterio_orden", configuracion.setCriterioOrden, methods=["POST"])
    app.add_url_rule("/configuracion/set/max-elementos", "config_set_max_elementos", configuracion.setMaxElementos, methods=["POST"])
    app.add_url_rule("/configuracion/set/mantenimiento", "config_toggle_mantenimiento", configuracion.toggleMaintenance)
    

    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("home.html")
    


    # Rutas de API-REST (usando Blueprints)
   

    # Handlers
    
    

    
    return app