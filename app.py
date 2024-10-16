from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, BigInteger, Boolean, ForeignKey
from flask_marshmallow import Marshmallow
from models import db
from schemas import ma
from routes import rosetas_bp, usuarios_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tester:test@localhost/test'

db.init_app(app)
ma.init_app(app)

# Rutas
app.register_blueprint(rosetas_bp, url_prefix='/api')
app.register_blueprint(usuarios_bp, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)


