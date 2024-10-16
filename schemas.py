from flask_marshmallow import Marshmallow
from models import Usuario, Roseta


ma = Marshmallow()

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True


class RosetaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Roseta
        load_instance = True
