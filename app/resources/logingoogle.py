from flask import current_app as app, url_for ,session,redirect
from authlib.integrations.flask_client import OAuth
from app.models.usuario import Usuario
from app.models.usuario_publico import Usuario_publico
from app.db import db
from datetime import datetime

oauth=OAuth(app)
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

def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


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
