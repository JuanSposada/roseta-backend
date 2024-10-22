from flask import Blueprint
from flask import Blueprint,jsonify, request
from models import ConfiguracionesRoseta
from schemas import ConfiguracionesRosetaSchema
from models import db

# Configuraciones Blueprint
configuracion_rosetas_bp = Blueprint('configuraciones_roseta',__name__)
@configuracion_rosetas_bp.route('/configuraciones-roseta', methods=['GET'])
def configuracion():
    configuracion_list = ConfiguracionesRoseta.query.all()
    configuracion_schema = ConfiguracionesRosetaSchema(many=True)
    result = configuracion_schema.dump(configuracion_list)
    return jsonify(result)