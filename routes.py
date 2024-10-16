from flask import Blueprint,jsonify
from models import Usuario, Roseta
from schemas import UsuarioSchema, RosetaSchema


#Blueprint de Usuarios
usuarios_bp = Blueprint('usuarios', __name__)
@usuarios_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios_list = Usuario.query.all()
    usuarios_schema = UsuarioSchema(many=True)
    result = usuarios_schema.dump(usuarios_list)
    return jsonify(result)



#Blueprint de Rosetas
rosetas_bp = Blueprint('rosetas', __name__)

@rosetas_bp.route('/rosetas', methods=['GET'])
def get_rosetas():
    rosetas_list = Roseta.query.all()
    rosetas_schema = RosetaSchema(many=True)
    result = rosetas_schema.dump(rosetas_list)
    return jsonify(result)
    

