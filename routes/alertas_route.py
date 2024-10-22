from flask import Blueprint,jsonify, request
from models import Alertas
from schemas import AlertasSchema
from models import db

# Blueprint alertas
alertas_bp = Blueprint('alertas', __name__)
@alertas_bp.route('/alertas', methods=['GET','POST'])
def alertas():
    alertas_list = Alertas.query.all()
    alertas_schema = AlertasSchema(many=True)
    result = alertas_schema.dump(alertas_list)
    return jsonify(result)