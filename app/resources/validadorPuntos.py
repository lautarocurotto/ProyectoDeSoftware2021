
from wtforms import validators, Form, StringField
from wtforms.fields.html5 import EmailField

class ValidarForm(Form):
    nombre=StringField('nombre', [
        validators.Required(message= 'El nombre es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    direccion=StringField('direccion', [
        validators.Required(message= 'La direccion es requerida'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    coordenadas=StringField('coordenadas', [
        validators.Required(message= 'Las coordenadas son requeridas'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    status=StringField('status', [
        validators.Required(message= 'El estado es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    telefono=StringField('telefono', [
        validators.Required(message= 'El telefono es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    email= EmailField('email',[
        validators.Required(message= 'El email es requerido'),
        validators.Email(message="Ingrese un email valido")])