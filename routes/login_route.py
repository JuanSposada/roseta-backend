from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import Usuario, db, Logs
from schemas import LoginSchema, UsuarioSchema
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token
from sqlalchemy import func

login_bp = Blueprint('login', __name__, 'Login dentro de la app')

@login_bp.route('/login')
class UserLogin(MethodView):
    @login_bp.arguments(LoginSchema)
    @login_bp.response(200)
    def post(self, data):
        usuario = Usuario.query.filter(Usuario.correo == data["correo"]).first()

        if usuario and pbkdf2_sha256.verify(data["password"], usuario.password):
            access_token = create_access_token(identity=usuario.id_usuario)
            usuario_data = UsuarioSchema().dump(usuario)
            id_usuario = usuario.id_usuario
            accion = 'Login exitoso'
            nuevo_log = Logs(id_usuario=id_usuario, accion=accion, fecha_hora=func.now())
            db.session.add(nuevo_log)
            db.session.commit()     
            return {"access_token": access_token}