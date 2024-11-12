from flask import jsonify, request
from models import  Dispositivo
from schemas import DispositivoSchema, DispositivoPostSchema
from models import db
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

 # Dispositivos   
dispositivos_bp = Blueprint('dispositivos', __name__, 'Operaciones con Dispositivos')
@dispositivos_bp.route('/dispositivos/get')
class Dispositivos(MethodView):
    @dispositivos_bp.response(200, DispositivoSchema)
    def get(self):
        """
        Obtiene la lista de todos los dispositivos registrados.

        **Respuesta exitosa (200):**
        Devuelve un listado con los detalles de todos los dispositivos.
        """
        dispositivos = Dispositivo.query.all()
        return dispositivos

@dispositivos_bp.route('/dispositivos/get/<string:id_dispositivo>')
class DispositivoSelect(MethodView):
    @dispositivos_bp.response(200, DispositivoSchema)    
    def get(self, id_dispositivo):
        dispositivo = Dispositivo.query.get_or_404(id_dispositivo)
        return dispositivo
    
@dispositivos_bp.route('/dispositivos/registrar')
class DispositivoRegistrar(MethodView):
    @dispositivos_bp.arguments(DispositivoPostSchema)
    @dispositivos_bp.response(201, DispositivoSchema)
    def post(self, dispositivo):
        try:
            db.session.add(dispositivo)
            db.session.commit()
        except SQLAlchemyError: 
            abort(500, message='Error al registrar dispositivo ')   
        return dispositivo    
    
    def put(self):
        if request.is_json:
            id_dispositivo = request.json['id_dispositivo']
            dispositivo = Dispositivo.query.filter_by(id_dispositivo=id_dispositivo).first()
            if dispositivo:
                try:
                    dispositivo.tipo_dispositivo = request.json['tipo_dispositivo']
                    dispositivo.estado_dispositivo = request.json['estado_dispositivo']
                    dispositivo.id_roseta = request.json['id_roseta']
                    db.session.commit()
                    return jsonify(message='updated')
                except KeyError:
                    return jsonify(message='formato, valores o tipo de dato incorrectos, solo se reciben JSON'),404

