
from wtforms import validators, Form, StringField


class ValidarForm(Form):
    nombre=StringField('nombre', [
        validators.DataRequired(message= 'El nombre es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    direccion=StringField('direccion', [
        validators.DataRequired(message= 'La direccion es requerida'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    lat=StringField('lat', [
       validators.DataRequired(message= 'Las coordenadas de latitud son requeridas'),
       validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    lng=StringField('lng', [
       validators.DataRequired(message= 'Las coordenadas de longitud son requeridas'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    status=StringField('status', [
        validators.DataRequired(message= 'El estado es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    telefono=StringField('telefono', [
        validators.DataRequired(message= 'El telefono es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    