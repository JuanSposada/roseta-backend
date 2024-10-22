from flask import Blueprint,jsonify, request
from models import HistorialSensores
from schemas import HistorialSensoresSchema
from models import db

# Historial Sensores
historial_sensores_bp = Blueprint('historial_sensores',__name__)
@historial_sensores_bp.route('/historial-sensores', methods=['GET'])
def historial_sensores():
    historial_list = HistorialSensores.query.all()
    historial_schema = HistorialSensoresSchema(many=True)
    result = historial_schema.dump(historial_list)
    return jsonify(result)