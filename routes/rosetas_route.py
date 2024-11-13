from models import Roseta
from schemas import RosetaSchema, RosetaPostSchema
from models import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# Blueprint de Rosetas
rosetas_bp = Blueprint('rosetas', __name__)

@rosetas_bp.route('/rosetas')
class Rosetas(MethodView):
    @rosetas_bp.response(200, RosetaSchema(many=True))
    def get(self):
        """Obtiene todos las Rosetas registradas en la Base de Datos"""
        rosetas = Roseta.query.all()
        return rosetas

@rosetas_bp.route('/rosetas/<string:id_roseta>')
class RosetaSelect(MethodView):
    @rosetas_bp.response(200, RosetaSchema)
    def get(self, id_roseta):
        """Obtiene solo la Roseta especificada en el parámetro si esta existe"""
        roseta = Roseta.query.get_or_404(id_roseta)
        return roseta

@rosetas_bp.route('/rosetas/get/<string:id_usuario>')
class RosetaUsuario(MethodView):
    @rosetas_bp.response(200, RosetaSchema(many=True))
    def get(self, id_usuario):
        """Obtiene  las Rosetas asociadas a un usuario si esta existe"""
        rosetas = Roseta.query.filter_by(id_usuario=id_usuario).all()
        if not rosetas:
            abort(404, message='no se encontro roseta')
        return rosetas


@rosetas_bp.route('/rosetas/update')
class RosetaUpdate(MethodView):
    @rosetas_bp.arguments(RosetaSchema)
    @rosetas_bp.response(200, RosetaSchema)
    def put(self, roseta_data):
        """
        Actualiza los datos de una roseta existente. Se puede actualizar la ubicación y el usuario asignado.
        Si el id_usuario proporcionado no existe, se genera un error.
        """
        id_roseta = roseta_data.id_roseta
        if not id_roseta:
            abort(400, message='Se requiere "id_roseta" para poder actualizar')

        roseta = Roseta.query.get(id_roseta)
        if not roseta:
            abort(404, message='id de roseta no encontrado') 
        
        for key, value in roseta_data.__dict__.items():
            if key != 'id_roseta' and hasattr(roseta, key):
                setattr(roseta, key, value)

        try:
            db.session.commit()

        except IntegrityError as e:
            db.session.rollback()
            if 'id_usuario' in str(e):
                abort(400, message="El usuario con el id especificado no existe")
            raise e
    
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Error al actualizar la roseta")

        return roseta

@rosetas_bp.route('/rosetas/registrar')
class RosetaRegistrar(MethodView):
    @rosetas_bp.arguments(RosetaPostSchema)
    @rosetas_bp.response(201, RosetaSchema)
    def post(self, roseta):
        """
        Registra una nueva roseta en la base de datos. Si ocurre un error, se devuelve un mensaje indicando el fallo.
        """
        try:
            db.session.add(roseta)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message='Error al registrar roseta')
        return roseta

@rosetas_bp.route('/rosetas/borrar/<string:id_roseta>')
class RosetaDelete(MethodView):
    @rosetas_bp.response(200, RosetaSchema)
    def delete(self, id_roseta):
        """
        Elimina una roseta de la base de datos. Si la roseta no existe, se devuelve un error 404.
        Si ocurre un error al eliminarla, se devuelve un error 400.
        """
        roseta = Roseta.query.get_or_404(id_roseta)
        try:
            db.session.delete(roseta)
            db.session.commit()
        except SQLAlchemyError:
            abort(400, message='Error al borrar roseta')
        return roseta
