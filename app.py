from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, BigInteger
from flask_marshmallow import Marshmallow


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tester:test@localhost/test'

db = SQLAlchemy(app)
ma = Marshmallow(app)


with app.app_context():
    try:
        db.engine.execute("SELECT 1")
        print("si")
    except:
        print('no')

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
    __tablename__ = 'usuarios_test'

    id_usuario = Column(BigInteger, primary_key=True)
    nombre = Column(Text, nullable=True)
    correo = Column(Text, unique=True, nullable=True)
    password = Column(Text, nullable=True )
    telefono = Column(Text, nullable=True)

# Clase para marshmallow

class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id_usuario', 'nombre', 'correo', 'password', 'telefono')

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)


if __name__ == '__main__':
    app.run(debug=True)


