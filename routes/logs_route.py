from flask import jsonify, request
from flask.views import MethodView
from models import Logs
from schemas import LogsSchema
from flask_smorest import Blueprint
from sqlalchemy import func

from models import db

#Blueprint de Logs
logs_bp = Blueprint('logs', __name__, description='operaciones relacionadas con Logs')
@logs_bp.route('/logs')
class Log(MethodView):
    def get(self):
        logs_list = Logs.query.all()
        logs_schema = LogsSchema(many=True)
        result = logs_schema.dump(logs_list)
        return jsonify(result)
    
    def post(self):
        if request.is_json:
            try:
                id_usuario = request.json["id_usuario"]
                accion = request.json["accion"]
                nuevo_log = Logs(id_usuario=id_usuario, accion=accion, fecha_hora=func.now())
                db.session.add(nuevo_log)
                db.session.commit()
                log_schema = LogsSchema()
                result = log_schema.dump(nuevo_log)
                return result, 201
            except:
                return jsonify(message='verifica datos correo debe ser unico'),400
        return jsonify(message="Solo se aceptan POST en formato JSON valido"),400
    