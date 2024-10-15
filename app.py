from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, BigInteger, Boolean, ForeignKey
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tester:test@localhost/test'

db = SQLAlchemy(app)
ma = Marshmallow(app)

# Rutas

@app.route('/api/sensors')
def sensores():
    return jsonify(mesage='sensor')

@app.route('/api/cameras')
def camaras():
    return jsonify(message='camara')

@app.route("/api/users", methods=['GET'])
def users():
    users_list = Usuario.query.all()
    result = usuarios_schema.dump(users_list)
    return jsonify(result)

@app.route("/api/rosetas", methods=['GET'])
def rosetas():
    rosetas_list = Roseta.query.all()
    result = rosetas_schema.dump(rosetas_list)
    return jsonify(result)


@app.route("/api/rosetas/add", methods=['POST'])
def rosetas_add():
    if request.is_json:
        ubicacion = request.json['ubicacion']
        estado = request.json['estado']
        id_usuario = request.json['id_usuario']
        roseta = Roseta(ubicacion=ubicacion, estado=estado, id_usuario=id_usuario)
        db.session.add(roseta)
        db.session.commit()
        return roseta_schema.jsonify(roseta)

@app.route("/api/users/<string:id>")
def users_id(id: str):
    return jsonify(user=id)

@app.route('/api/alerts')
def alerts():
    return jsonify(message='alerts')

@app.route('/api/wifi')
def wifi():
    return jsonify(message='wifi')

@app.route('/api/not-found')
def not_found():
    return jsonify(message='request not found'), 404

# modelos de base de datos
class Usuario(db.Model): 
    __tablename__ = 'usuarios'

    id_usuario = Column(BigInteger, primary_key=True)
    nombre = Column(Text, nullable=True)
    correo = Column(Text, unique=True, nullable=True)
    password = Column(Text, nullable=True )
    telefono = Column(Text, nullable=True)

class Roseta(db.Model):
    __tablename__= 'rosetas'
    id_roseta = Column(BigInteger, primary_key=True)
    ubicacion = Column(Text, nullable=True)
    estado = Column(Boolean)
    id_usuario = Column(BigInteger, ForeignKey('usuarios.id_usuario'), nullable=False)

# Clase para marshmallow

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id_usuario', 'nombre', 'correo', 'password', 'telefono')

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)

class RosetaSchema(ma.Schema):
    class Meta:
        fields = ('id_roseta', 'ubicacion','estado','id_usuario')
roseta_schema = RosetaSchema()
rosetas_schema = RosetaSchema(many=True)


if __name__ == '__main__':
    app.run(debug=True)


