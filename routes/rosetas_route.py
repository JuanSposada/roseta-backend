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
        """Obtiene todas las Rosetas registradas en la Base de Datos
        ---
        Devuelve una lista de todas las Rosetas disponibles.
        """
        rosetas = Roseta.query.all()
        return rosetas

@rosetas_bp.route('/rosetas/<string:id_roseta>')
class RosetaSelect(MethodView):
    @rosetas_bp.response(200, RosetaSchema)
    def get(self, id_roseta):
        """Obtiene una Roseta específica
        ---
        Parámetros:
          - id_roseta (string): ID de la roseta que se desea consultar.
        
        Devuelve la Roseta especificada en el parámetro si esta existe. 
        En caso contrario, retorna un error 404.
        """
        roseta = Roseta.query.get_or_404(id_roseta)
        return roseta

@rosetas_bp.route('/rosetas/update')
class RosetaUpdate(MethodView):
    @rosetas_bp.arguments(RosetaSchema)
    @rosetas_bp.response(200, RosetaSchema)
    def put(self, roseta_data):
        """Actualiza una Roseta existente
        ---
        Parámetros:
          - id_roseta (string): ID de la roseta a actualizar. Este debe existir en la base de datos.
          - otros campos de Roseta para actualizar (ubicación, id_usuario, etc.)

        Actualiza los datos de una Roseta. Si el `id_roseta` o `id_usuario` proporcionados no existen, se genera un error.
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
        """Registra una nueva Roseta
        ---
        Registra una nueva Roseta en la base de datos. Si ocurre un error, se devuelve un mensaje indicando el fallo.
        
        Parámetros:
          - Datos de la Roseta (ubicación, id_usuario, etc.)
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
        """Elimina una Roseta existente
        ---
        Parámetros:
          - id_roseta (string): ID de la roseta que se desea eliminar.
        
        Elimina una roseta de la base de datos. Si la roseta no existe, se devuelve un error 404.
        """
        roseta = Roseta.query.get_or_404(id_roseta)
        try:
            db.session.delete(roseta)
            db.session.commit()
        except SQLAlchemyError:
            abort(400, message='Error al borrar roseta')
        return roseta
