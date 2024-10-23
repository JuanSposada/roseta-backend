from flask import Blueprint,jsonify, request
from models import Roseta
from schemas import RosetaSchema
from models import db

#Blueprint de Rosetas
rosetas_bp = Blueprint('rosetas', __name__)
@rosetas_bp.route('/rosetas', methods=['GET', 'POST'])
def rosetas():
    if request.method == 'GET':
        rosetas_list = Roseta.query.all()
        rosetas_schema = RosetaSchema(many=True)
        result = rosetas_schema.dump(rosetas_list)
        return jsonify(result)
    if request.method == 'POST':
        if request.is_json:
                ubicacion = request.json['ubicacion']
                estado = request.json['estado']
                id_usuario = request.json['id_usuario']
                roseta = Roseta(ubicacion=ubicacion, estado=estado, id_usuario=id_usuario)
                db.session.add(roseta)
                db.session.commit()
                roseta_schema = RosetaSchema()
                result = roseta_schema.dump(roseta)
                return jsonify(result),201
        return jsonify(message="Solo se aceptan POST en formato JSON valido"),400