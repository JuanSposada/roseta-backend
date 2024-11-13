from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import Usuario
from schemas import LoginSchema, UsuarioSchema
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token

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
            return {"access_token": access_token,
                    "usuario": usuario_data}