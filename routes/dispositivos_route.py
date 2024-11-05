from flask import jsonify, request
from models import  Dispositivo
from schemas import DispositivoSchema
from models import db
from flask_smorest import Blueprint
from flask.views import MethodView

 # Dispositivos   
dispositivos_bp = Blueprint('dispositivos', __name__, 'Operaciones con Dispositivos')
@dispositivos_bp.route('/dispositivos')
class Dispositivos(MethodView):
    def get(self):
        dispositivos_list = Dispositivo.query.all()
        dispositivos_schema = DispositivoSchema(many=True)
        result = dispositivos_schema.dump(dispositivos_list)
        return jsonify(result)
    
    def post(self):
        if request.is_json:
            tipo_dispositivo = request.json['tipo_dispositivo']
            estado_dispositivo = request.json['estado_dispositivo']
            id_roseta = request.json['id_roseta']
            dispositivo = Dispositivo(tipo_dispositivo=tipo_dispositivo, estado_dispositivo=estado_dispositivo, id_roseta=id_roseta)
            db.session.add(dispositivo)
            db.session.commit()
            dispositivo_schema = DispositivoSchema()
            result = dispositivo_schema.dump(dispositivo)
            return jsonify(result),201
        return jsonify(message="Solo se aceptan POST en formato JSON valido"),400
    
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

