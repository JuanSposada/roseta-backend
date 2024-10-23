from flask import Blueprint,jsonify, request
from models import Alertas
from schemas import AlertasSchema
from models import db

# Blueprint alertas
alertas_bp = Blueprint('alertas', __name__)
@alertas_bp.route('/alertas', methods=['GET','POST'])
def alertas():
    if request.method == 'GET':
        alertas_list = Alertas.query.all()
        alertas_schema = AlertasSchema(many=True)
        result = alertas_schema.dump(alertas_list)
        return jsonify(result)
    if request.method == 'POST':
        tipo_alerta = request.json['tipo_alerta']
        mensaje = request.json['mensaje']
        fecha_hora = request.json['fecha_hora']
        id_roseta = request.json['id_roseta']
        alerta = Alertas(tipo_alerta=tipo_alerta, mensaje=mensaje, fecha_hora=fecha_hora, id_roseta=id_roseta)
        db.session.add(alerta)
        db.session.commit()
        alerta_schema = AlertasSchema()
        result = alerta_schema.dump(alerta)
        return jsonify(result),201
    return jsonify(message="Solo se aceptan POST en formato JSON valido"),400