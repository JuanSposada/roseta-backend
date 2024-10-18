from flask_marshmallow import Marshmallow
from models import Usuario, Roseta, Dispositivo,HistorialSensores


ma = Marshmallow()

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True


class RosetaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Roseta
        load_instance = True

class DispositivoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dispositivo
        load_instance = True

class HistorialSensoresSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = HistorialSensores
        load_instance = True