from flask import Blueprint,jsonify, request
from models import Usuario
from schemas import UsuarioSchema
from models import db


#Blueprint de Usuarios
usuarios_bp = Blueprint('usuarios', __name__)
@usuarios_bp.route('/usuarios', methods=['GET','POST','PUT', 'DELETE'])
def usuarios():
    if request.method == 'GET':
        usuarios_list = Usuario.query.all()
        usuarios_schema = UsuarioSchema(many=True)
        result = usuarios_schema.dump(usuarios_list)
        return jsonify(result)
    
    if request.method == 'POST':
        if request.is_json:
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
            return jsonify(result)

        return jsonify(message='metodo post')
    