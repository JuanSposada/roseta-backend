from flask_smorest import Blueprint, abort
from flask.views import MethodView
from models import Usuario
from schemas import LoginSchema
from passlib.hash import pbkdf2_sha256

login_bp = Blueprint('login', __name__, 'Login dentro de la app')

@login_bp.route('/login')
class UserLogin(MethodView):
    @login_bp.arguments(LoginSchema)
    def post(self, data):
        usuario = Usuario.query.filter(Usuario.correo == data["correo"]).first()

        if usuario and pbkdf2_sha256.verify(data["password"], usuario.password):
            return "Si pase por aqui se verifico password"
