from wtforms import validators, Form, StringField


class ValidarForm(Form):
    nombre=StringField('nombre', [
        validators.DataRequired(message= 'El nombre es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    descripcion=StringField('descripcion', [
        validators.DataRequired(message= 'La descripcion es requerida'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    status=StringField('status', [
        validators.DataRequired(message= 'El estado es requerido'),
        validators.Length(min=1, max=255,message="La longitud debe ser entre 1 y 255 caracteres")
    ])
    
 