from flask import jsonify, request
from flask.views import MethodView
from models import Usuario
from schemas import UsuarioSchema
from flask_smorest import Blueprint

from models import db


#Blueprint de Usuarios
usuarios_bp = Blueprint('usuarios', __name__)
@usuarios_bp.route('/usuarios')
class Usuarios(MethodView):
    def get(self):
        usuarios_list = Usuario.query.all()
        usuarios_schema = UsuarioSchema(many=True)
        result = usuarios_schema.dump(usuarios_list)
        return jsonify(result)
    
    def post(self):
        if request.is_json:
            try:
                nombre = request.json['nombre']
                correo = request.json['correo']
                password = request.json['password']
                telefono = request.json['telefono']
                rol = request.json['rol']
                usuario = Usuario(nombre=nombre, correo=correo, password=password,telefono=telefono, rol=rol)
                db.session.add(usuario)
                db.session.commit()
                usuario_schema = UsuarioSchema()
                result = usuario_schema.dump(usuario)
                return jsonify(result),201
            except:
                return jsonify(message='verifica datos correo debe ser unico'),400
        return jsonify(message="Solo se aceptan POST en formato JSON valido"),400

@usuarios_bp.route('/usuarios/<string:id_usuario>')
class UsuarioSelect(MethodView):
    def put(self, id_usuario):
        return jsonify(message='put' + id_usuario)
    
    def delete(self, id_usuario):
        return jsonify(message='delete' + id_usuario)
