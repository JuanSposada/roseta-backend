from flask import jsonify, request
from models import Roseta
from schemas import RosetaSchema
from models import db
from flask_smorest import Blueprint
from flask.views import MethodView

#Blueprint de Rosetas
rosetas_bp = Blueprint('rosetas', __name__)
@rosetas_bp.route('/rosetas')
class Rosetas(MethodView):
    
    def get(self):
        rosetas_list = Roseta.query.all()
        rosetas_schema = RosetaSchema(many=True)
        result = rosetas_schema.dump(rosetas_list)
        return jsonify(result)
    
    def post(self):
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
    
    def put(self):
        if request.json:
            id_roseta = request.json['id_roseta']
            roseta = Roseta.query.filter_by(id_roseta=id_roseta).first()
            if roseta:
                roseta.ubicacion = request.json['ubicacion']
                roseta.estado = request.json['estado']
                roseta.id_usuario = request.json['id_usuario']
                db.session.commit()
                return jsonify(message='updated')
    
    def delete(self, id_roseta):
        return jsonify(message='delete' + id_roseta)
    
#@rosetas_bp.route('/rosetas/<string:id_roseta>')
#class RosetaModify(MethodView):
    

        
     