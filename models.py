from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, BigInteger, Boolean, ForeignKey


db = SQLAlchemy()

class Roseta(db.Model):
    __tablename__= 'rosetas'
    id_roseta = Column(BigInteger, primary_key=True)
    ubicacion = Column(Text, nullable=True)
    estado = Column(Boolean)
    id_usuario = Column(BigInteger, ForeignKey('usuarios.id_usuario'), nullable=False)


class Usuario(db.Model): 
    __tablename__ = 'usuarios'

    id_usuario = Column(BigInteger, primary_key=True)
    nombre = Column(Text, nullable=True)
    correo = Column(Text, unique=True, nullable=True)
    password = Column(Text, nullable=True )
    telefono = Column(Text, nullable=True)