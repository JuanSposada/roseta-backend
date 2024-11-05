from flask import jsonify, request
from models import HistorialSensores
from schemas import HistorialSensoresSchema
from models import db
from flask.views import MethodView
from flask_smorest import Blueprint

# Historial Sensores
historial_sensores_bp = Blueprint('historial_sensores',__name__, description='Historial de eventos de sensores')
@historial_sensores_bp.route('/historial-sensores')
class HistSensor(MethodView):
    def get(self):
        historial_list = HistorialSensores.query.all()
        historial_schema = HistorialSensoresSchema(many=True)
        result = historial_schema.dump(historial_list)
        return jsonify(result)
    
    def post(self):
        if request.is_json:
            tipo_sensor = request.json['tipo_sensor']
            fecha_hora = request.json['fecha_hora']
            valor = request.json['valor']
            id_roseta = request.json['id_roseta']
            hist_sensor = HistorialSensores(tipo_sensor=tipo_sensor, fecha_hora=fecha_hora, valor=valor, id_roseta=id_roseta)
            db.session.add(hist_sensor)
            db.session.commit()
            hist_sensor_schema = HistorialSensoresSchema()
            result = hist_sensor_schema.dump(hist_sensor)
            return jsonify(result),201
        return jsonify(message="Solo se aceptan POST en formato JSON valido"),400