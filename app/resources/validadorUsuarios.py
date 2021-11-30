from wtforms import validators, Form, StringField


class ValidarForm(Form):
    username = StringField(
        "username",
        [
            validators.DataRequired(message="El nombre de usuario es requerido"),
            validators.Length(
                min=1, max=255, message="La longitud debe ser entre 1 y 255 caracteres"
            ),
        ],
    )
    password = StringField(
        "password",
        [
            validators.DataRequired(message="La contraseña es requerida"),
            validators.Length(
                min=1, max=255, message="La longitud debe ser entre 1 y 255 caracteres"
            ),
        ],
    )
    name = StringField(
        "name",
        [
            validators.DataRequired(message="El nombre es requerido"),
            validators.Length(
                min=1, max=255, message="La longitud debe ser entre 1 y 255 caracteres"
            ),
        ],
    )
    lastname = StringField(
        "lastname",
        [
            validators.DataRequired(message="El apellido es requerido"),
            validators.Length(
                min=1, max=255, message="La longitud debe ser entre 1 y 255 caracteres"
            ),
        ],
    )
