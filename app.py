from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, BigInteger, Boolean, ForeignKey
from flask_marshmallow import Marshmallow
from models import db
from schemas import ma
from routes import  register_blueprints


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tester:test@localhost/test'

db.init_app(app)
ma.init_app(app)

#registrar blueprints
register_blueprints(app)


# Rutas


if __name__ == '__main__':
    app.run(debug=True)


