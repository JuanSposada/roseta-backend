from flask import Blueprint,jsonify, request
from models import  Dispositivo
from schemas import DispositivoSchema
from models import db

 # Dispositivos   
dispositivos_bp = Blueprint('dispositivos', __name__)
@dispositivos_bp.route('/dispositivos', methods=['GET'])
def dispositivos():
    dispositivos_list = Dispositivo.query.all()
    dispositivos_schema = DispositivoSchema(many=True)
    result = dispositivos_schema.dump(dispositivos_list)
    return jsonify(result)