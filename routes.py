from flask import Blueprint,jsonify, request
from models import Usuario, Roseta, Dispositivo, HistorialSensores
from schemas import UsuarioSchema, RosetaSchema, DispositivoSchema, HistorialSensoresSchema


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


#Blueprint de Rosetas
rosetas_bp = Blueprint('rosetas', __name__)
@rosetas_bp.route('/rosetas', methods=['GET'])
def rosetas():
    rosetas_list = Roseta.query.all()
    rosetas_schema = RosetaSchema(many=True)
    result = rosetas_schema.dump(rosetas_list)
    return jsonify(result)
    
 # Dispositivos   
dispositivos_bp = Blueprint('dispositivos', __name__)
@dispositivos_bp.route('/dispositivos', methods=['GET'])
def dispositivos():
    dispositivos_list = Dispositivo.query.all()
    dispositivos_schema = DispositivoSchema(many=True)
    result = dispositivos_schema.dump(dispositivos_list)
    return jsonify(result)

# Historial Sensores
historial_sensores_bp = Blueprint('historial_senores',__name__)
@historial_sensores_bp.route('/historial-sensores', methods=['GET'])
def historial_sensores():
    historial_list = HistorialSensores.query.all()
    historial_schema = HistorialSensoresSchema(many=True)
    result = historial_schema.dump(historial_list)
    return jsonify(result)
