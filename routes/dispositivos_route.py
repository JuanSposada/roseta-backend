from flask import Blueprint,jsonify, request
from models import  Dispositivo
from schemas import DispositivoSchema
from models import db

 # Dispositivos   
dispositivos_bp = Blueprint('dispositivos', __name__)
@dispositivos_bp.route('/dispositivos', methods=['GET','POST'])
def dispositivos():
    if request.method == 'GET':
        dispositivos_list = Dispositivo.query.all()
        dispositivos_schema = DispositivoSchema(many=True)
        result = dispositivos_schema.dump(dispositivos_list)
        return jsonify(result)
    if request.method == 'POST':
        if request.is_json:
            tipo_dispositivo = request.json['tipo_dispositivo']
            estado_dispositivo = request.json['estado_dispositivo']
            id_roseta = request.json['id_roseta']
            dispositivo = Dispositivo(tipo_dispositivo=tipo_dispositivo, estado_dispositivo=estado_dispositivo, id_roseta=id_roseta)
            db.session.add(dispositivo)
            db.session.commit()
            dispositivo_schema = DispositivoSchema()
            result = dispositivo_schema.dump(dispositivo)
            return jsonify(result)