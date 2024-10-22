from flask import Blueprint,jsonify, request
from models import Usuario
from schemas import UsuarioSchema
from models import db


#Blueprint de Usuarios
usuarios_bp = Blueprint('usuarios', __name__)
@usuarios_bp.route('/usuarios', methods=['GET','POST'])
def usuarios():
    if request.method == 'GET':
        usuarios_list = Usuario.query.all()
        usuarios_schema = UsuarioSchema(many=True)
        result = usuarios_schema.dump(usuarios_list)
        return jsonify(result)
    
    if request.method == 'POST':
        return jsonify(message='metodo post')