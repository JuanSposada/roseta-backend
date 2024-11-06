from flask import jsonify, request
from flask.views import MethodView
from models import Usuario
from schemas import UsuarioSchema
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
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
    
    def put(self):
        if request.is_json:
            id_usuario = request.json['id_usuario']
            usuario = Usuario.query.filter_by(id_usuario=id_usuario).first()
            if usuario:
                usuario.nombre = request.json['nombre']
                usuario.correo = request.json['correo']
                usuario.rol = request.json['rol']
                usuario.password = request.json['password']
                usuario.telefono = request.json['telefono']
                db.session.commit()
                return jsonify(message='updated')

@usuarios_bp.route('/usuarios/registrar')
class UsuarioSelect(MethodView):
    @usuarios_bp.arguments(UsuarioSchema)
    @usuarios_bp.response(201, UsuarioSchema)
    def post(self, usuario):
        try:
            db.session.add(usuario)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message='Error al registrar usuario')
        return usuario