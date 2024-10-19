from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, BigInteger, Boolean, ForeignKey,TIMESTAMP


db = SQLAlchemy()

class Usuario(db.Model): 
    __tablename__ = 'usuarios'

    id_usuario = Column(BigInteger, primary_key=True)
    nombre = Column(Text, nullable=False)
    correo = Column(Text, unique=True, nullable=False)
    password = Column(Text, nullable=False )
    telefono = Column(Text, nullable=True)
    rol = Column(Text, nullable=True)

class Roseta(db.Model):
    __tablename__= 'rosetas'
    id_roseta = Column(BigInteger, primary_key=True)
    ubicacion = Column(Text, nullable=True)
    estado = Column(Boolean)
    id_usuario = Column(BigInteger, ForeignKey('usuarios.id_usuario'), nullable=False)

class Dispositivo(db.Model):
    __tablename__= 'dispositivos'
    id_dispositivo = Column(BigInteger, primary_key=True, autoincrement=True)
    tipo_dispositivo = Column(Text, nullable=False)
    estado_dispositivo= Column(Boolean)
    id_roseta = Column(BigInteger, ForeignKey('rosetas.id_roseta'))

class HistorialSensores(db.Model):
    __tablename__ = 'historial_sensores'
    id_historial = Column(BigInteger, primary_key=True)
    tipo_sensor = Column(Text, nullable=False)
    fecha_hora = Column(TIMESTAMP, nullable=False)
    valor = Column(Text, nullable=False)
    id_roseta = Column(BigInteger, ForeignKey('rosetas.id_roseta'), nullable=False)

class HistorialCamaras(db.Model):
    __tablenae__ = 'historial_camaras'
    id_evento = Column(BigInteger, primary_key=True)
    fecha_hora = Column(TIMESTAMP, nullable=False)
    tipo_evento = Column(Text, nullable=False)
    url_video = Column(Text, nullable=False)
    id_roseta = Column(BigInteger, ForeignKey('rosetas.id_roseta'), nullable=False)

