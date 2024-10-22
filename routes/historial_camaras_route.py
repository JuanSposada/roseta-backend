from flask import Blueprint, jsonify, request
from models import HistorialCamaras
from schemas import HistorialCamarasSchema

# Blueprint historial_camaras
historial_camaras_bp = Blueprint('historial_camaras',__name__)
@historial_camaras_bp.route('/historial-camaras', methods=['GET'])
def historial_camaras():
    historial_camaras_list = HistorialCamaras.query.all()
    historial_camaras_schema = HistorialCamarasSchema(many=True)
    result = historial_camaras_schema.dump(historial_camaras_list)
    return jsonify(result)