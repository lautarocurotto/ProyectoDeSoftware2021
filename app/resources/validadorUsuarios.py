from wtforms import validators, Form, StringField
from wtforms.fields.html5 import EmailField

class ValidarForm(Form):
    username=StringField('username', [
        validators.Required(message= 'El nombre de usuario es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    password=StringField('password', [
        validators.Required(message= 'La contraseña es requerida'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    name=StringField('name', [
        validators.Required(message= 'El nombre es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    lastname=StringField('lastname', [
        validators.Required(message= 'El apellido es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    
    email= EmailField('email',[
        validators.Required(message= 'El email es requerido'),
        validators.Email(message="Ingrese un email valido")])
