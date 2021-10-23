from wtforms import validators, Form, StringField


class ValidarForm(Form):
    nombre=StringField('nombre', [
        validators.Required(message= 'El nombre es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    descripcion=StringField('descripcion', [
        validators.Required(message= 'La descripcion es requerida'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    lat=StringField('lat', [
        validators.Required(message= 'Las coordenadas lat son requeridas'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    lng=StringField('lng', [
        validators.Required(message= 'Las coordenadas lng son requeridas'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    status=StringField('status', [
        validators.Required(message= 'El estado es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    
 