from flask import jsonify, request
from models import ConfiguracionesRoseta
from schemas import ConfiguracionesRosetaSchema
from models import db
from flask_smorest import Blueprint
from flask.views import MethodView

# Configuraciones Blueprint
configuracion_rosetas_bp = Blueprint('configuraciones_roseta',__name__,'operaciones de configuracion de roseta')
@configuracion_rosetas_bp.route('/configuraciones-roseta')
class Configuracion(MethodView):
    def get(self):
        configuraciones_list = ConfiguracionesRoseta.query.all()
        configuraciones_schema = ConfiguracionesRosetaSchema(many=True)
        result = configuraciones_schema.dump(configuraciones_list)
        return jsonify(result)
    
    def post(self):
        if request.is_json:
            try:
                id_roseta = request.json['id_roseta']
                wifi_ssid = request.json['wifi_ssid']
                wifi_password = request.json['wifi_password']
                umbral_humo = request.json['umbral_humo']
                umbral_movimiento = request.json['umbral_movimiento']
                configuraciones = ConfiguracionesRoseta(id_roseta=id_roseta,wifi_ssid=wifi_ssid, wifi_password=wifi_password, umbral_humo=umbral_humo, umbral_movimiento=umbral_movimiento)
                db.session.add(configuraciones)
                db.session.commit()
                configuracion_schema = ConfiguracionesRosetaSchema()
                result = configuracion_schema.dump(configuraciones)
                return jsonify(result),201
            except KeyError:
                return jsonify(message='revisa el formato de tus datos'),401
        return jsonify(message='Solo se aceptan JSON validos'),400
    
    def put(self):
        if request.is_json:
            id_configuracion = request.json['id_configuracion']
            configuracion = ConfiguracionesRoseta.query.filter_by(id_configuracion=id_configuracion).first()
            if configuracion:
                configuracion.id_roseta = request.json['id_roseta']
                configuracion.wifi_ssid = request.json['wifi_ssid']
                configuracion.wifi_password = request.json['wifi_password']
                configuracion.umbral_humo = request.json['umbral_humo']
                configuracion.umbral_movimiento = request.json['umbral_movimiento']
                db.session.commit()
                return jsonify(message='update')
        return jsonify(message='Solo se acepta formato JSON')