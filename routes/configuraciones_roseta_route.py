from flask import jsonify, request
from models import ConfiguracionesRoseta
from schemas import ConfiguracionesRosetaSchema
from models import db
from flask_smorest import Blueprint

# Configuraciones Blueprint
configuracion_rosetas_bp = Blueprint('configuraciones_roseta',__name__)
@configuracion_rosetas_bp.route('/configuraciones-roseta', methods=['GET','POST'])
def configuracion():
    if request.method =='GET':
        configuraciones_list = ConfiguracionesRoseta.query.all()
        configuraciones_schema = ConfiguracionesRosetaSchema(many=True)
        result = configuraciones_schema.dump(configuraciones_list)
        return jsonify(result)
    if request.method == 'POST':
        if request.is_json:
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
        return jsonify(message='Solo se aceptan JSON validos'),400