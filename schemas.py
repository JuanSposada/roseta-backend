from flask_marshmallow import Marshmallow
from models import Usuario, Roseta, Dispositivo,HistorialSensores, HistorialCamaras, ConfiguracionesRoseta, Alertas, Logs, db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, Schema


ma = Marshmallow()

class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
        include_fk = True
        sqla_session = db.session

class UsuariosPostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        load_instance = True
        include_fk = True
        sqla_session = db.session
        exclude = ('id_usuario',)

class RosetaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Roseta
        load_instance = True
        include_fk = True
        sqla_session = db.session

class RosetaPostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Roseta
        load_instance = True
        include_fk = True
        sqla_session = db.session
        exclude=('id_roseta',)

class DispositivoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Dispositivo
        load_instance = True
        include_fk = True

class DispositivoPostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Dispositivo
        load_instance = True
        include_fk = True
        exclude=('id_dispositivo',)


class HistorialSensoresSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = HistorialSensores
        load_instance = True
        include_fk = True

class HistorialCamarasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = HistorialCamaras
        load_instance = True
        include_fk = True

class ConfiguracionesRosetaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ConfiguracionesRoseta
        load_instance = True
        include_fk = True

class AlertasSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Alertas
        load_instance = True
        include_fk = True

class LogsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Logs
        load_instance = True
        include_fk = True

class LoginSchema(Schema):
    correo = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)