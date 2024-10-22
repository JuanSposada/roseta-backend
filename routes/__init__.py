from .usuarios_route import usuarios_bp
from .rosetas_route import rosetas_bp
from .dispositivos_route import dispositivos_bp
from .historial_sensores_route import historial_sensores_bp
from .historial_camaras_route import historial_camaras_bp
from .configuraciones_roseta_route import configuracion_rosetas_bp
from .alertas_route import alertas_bp


# Registrar blueprints
def register_blueprints(app):
    app.register_blueprint(usuarios_bp, url_prefix='/api')
    app.register_blueprint(rosetas_bp, url_prefix='/api')
    app.register_blueprint(dispositivos_bp, url_prefix='/api')
    app.register_blueprint(historial_sensores_bp, url_prefix='/api')
    app.register_blueprint(historial_camaras_bp, url_prefix='/api')
    app.register_blueprint(configuracion_rosetas_bp, url_prefix='/api')
    app.register_blueprint(alertas_bp, url_prefix='/api')
    