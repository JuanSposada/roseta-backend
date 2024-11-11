from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Text, BigInteger, Boolean, ForeignKey,TIMESTAMP, Integer
from sqlalchemy.sql import func

db = SQLAlchemy()

class Usuario(db.Model): 
    __tablename__ = 'usuarios'

    id_usuario = Column(BigInteger, primary_key=True)
    nombre = Column(Text, nullable=False)
    correo = Column(Text, unique=True, nullable=False)
    password = Column(Text, nullable=False)
    telefono = Column(Text)
    rol = Column(Text)

    #Relaciones DB
    logs = db.relationship('Logs', back_populates='usuario')
    rosetas = db.relationship("Roseta", back_populates="usuario")

class Roseta(db.Model):
    __tablename__= 'rosetas'
    id_roseta = Column(BigInteger, primary_key=True, autoincrement=True)
    ubicacion = Column(Text, nullable=False)
    estado = Column(Boolean)
    id_usuario = Column(BigInteger, ForeignKey('usuarios.id_usuario'), nullable=False)
    
    #Relaciones con la DB
    usuario = db.relationship("Usuario", back_populates='rosetas')
    dispositivos = db.relationship('Dispositivo', back_populates='roseta')
    historial_sensores = db.relationship('HistorialSensores', back_populates='roseta')
    historial_camaras = db.relationship('HistorialCamaras', back_populates='roseta')
    configuraciones = db.relationship('ConfiguracionesRoseta', back_populates='roseta')
    alertas = db.relationship('Alertas', back_populates='roseta')
    
    

class Dispositivo(db.Model):
    __tablename__= 'dispositivos'
    id_dispositivo = Column(BigInteger, primary_key=True, autoincrement=True)
    tipo_dispositivo = Column(Text, nullable=False)
    estado_dispositivo= Column(Boolean)
    id_roseta = Column(BigInteger, ForeignKey('rosetas.id_roseta'), nullable=False)
    roseta = db.relationship('Roseta', back_populates='dispositivos')

class HistorialSensores(db.Model):
    __tablename__ = 'historial_sensores'
    id_historial = Column(BigInteger, primary_key=True)
    tipo_sensor = Column(Text, nullable=False)
    fecha_hora = Column(TIMESTAMP, nullable=False)
    valor = Column(Text, nullable=False)
    id_roseta = Column(BigInteger, ForeignKey('rosetas.id_roseta'), nullable=False)
    roseta = db.relationship('Roseta', back_populates='historial_sensores')

class HistorialCamaras(db.Model):
    __tablename__ = 'historial_camaras'
    id_evento = Column(BigInteger, primary_key=True)
    fecha_hora = Column(TIMESTAMP, nullable=False)
    tipo_evento = Column(Text, nullable=False)
    url_video = Column(Text, nullable=False)
    id_roseta = Column(BigInteger, ForeignKey('rosetas.id_roseta'), nullable=False)
    roseta = db.relationship('Roseta', back_populates='historial_camaras')


class ConfiguracionesRoseta(db.Model):
    __tablename__ = 'configuraciones_roseta'
    id_configuracion = Column(BigInteger, primary_key=True)
    id_roseta = Column(BigInteger, ForeignKey('rosetas.id_roseta'), nullable=False)
    wifi_ssid = Column(Text, nullable=False)
    wifi_password = Column(Text, nullable=False)
    umbral_humo = Column(Integer, nullable=False)
    umbral_movimiento = Column(Integer, nullable=False)
    roseta = db.relationship('Roseta', back_populates='configuraciones')
 
class Alertas(db.Model):
    __tablename__ = 'alertas'
    id_alerta = Column(BigInteger, primary_key=True)
    tipo_alerta = Column(Text, nullable=False)
    mensaje = Column(Text, nullable=False)
    fecha_hora = Column(TIMESTAMP, nullable=False)
    id_roseta = Column(BigInteger, ForeignKey('rosetas.id_roseta'), nullable=False)
    roseta = db.relationship('Roseta', back_populates='alertas')

class Logs(db.Model):
    __tablename__ = 'logs'
    id_log = Column(BigInteger, primary_key=True)
    id_usuario = Column(BigInteger, ForeignKey('usuarios.id_usuario'), nullable=False)
    fecha_hora = Column(TIMESTAMP, server_default=func.now())
    accion = Column(Text)
    usuario = db.relationship('Usuario', back_populates='logs')
