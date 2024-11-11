from flask.views import MethodView
from models import Usuario
from schemas import UsuarioSchema, UsuariosPostSchema
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from models import db

# Blueprint de Usuarios
usuarios_bp = Blueprint('usuarios', __name__, description='Operaciones con Usuarios')

# Endpoint para obtener todos los usuarios
@usuarios_bp.route('/usuarios/get')
class Usuarios(MethodView):
    @usuarios_bp.response(200, UsuarioSchema(many=True))
    def get(self):
        """
        Obtiene la lista de todos los usuarios registrados.

        **Respuesta exitosa (200):**
        Devuelve un listado con los detalles de todos los usuarios.
        """
        usuarios = Usuario.query.all()
        return usuarios
    
# Endpoint para obtener un usuario por su ID
@usuarios_bp.route('/usuarios/get/<string:usuario_id>')
class UsuarioSelect(MethodView):
    @usuarios_bp.response(200, UsuarioSchema)
    def get(self, usuario_id):
        """
        Obtiene los detalles de un usuario específico por su ID.

        :param usuario_id: El ID único del usuario.
        
        **Respuesta exitosa (200):**
        Devuelve los detalles del usuario solicitado.
        
        **Error 404:**
        Si el ID de usuario no existe en la base de datos.
        """
        usuario = Usuario.query.get_or_404(usuario_id)
        return usuario


# Endpoint para registrar un nuevo usuario
@usuarios_bp.route('/usuarios/registrar')
class UsuarioRegister(MethodView):
    @usuarios_bp.arguments(UsuariosPostSchema)
    @usuarios_bp.response(201, UsuarioSchema)
    def post(self, usuario):
        """
        Registra un nuevo usuario en el sistema.

        **Datos requeridos en el cuerpo de la solicitud (formato JSON):**
        - `nombre`: Nombre completo del usuario.
        - `correo`: Correo electrónico del usuario.

        **Respuesta exitosa (201):**
        Devuelve los detalles del nuevo usuario creado.

        **Error 500:**
        Si ocurre un error al guardar el usuario en la base de datos.
        """
        try:
            db.session.add(usuario)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message='Error al registrar usuario')
        return usuario

# Endpoint para actualizar los datos de un usuario
@usuarios_bp.route('/usuarios/update')
class UsuarioUpdate(MethodView):
    @usuarios_bp.arguments(UsuarioSchema)
    @usuarios_bp.response(200, UsuarioSchema)
    def put(self, user_data):
        """
        Actualiza los datos de un usuario existente.

        **Datos requeridos en el cuerpo de la solicitud (formato JSON):**
        - `id_usuario`: ID del usuario a actualizar.
        - Se pueden actualizar otros campos, como `nombre`, `correo`, etc.

        **Respuesta exitosa (200):**
        Devuelve los detalles del usuario actualizado.

        **Error 400:**
        Si no se incluye el `id_usuario` o si los datos no cumplen con las restricciones (por ejemplo, correo duplicado).

        **Error 404:**
        Si no se encuentra el usuario con el `id_usuario` especificado.

        **Error 500:**
        Si ocurre un error en la base de datos al intentar actualizar el usuario.
        """
        id_usuario = user_data.id_usuario
        if not id_usuario:
            abort(400, message='Se requiere "id_usuario" para poder actualizar')

        usuario = Usuario.query.get(id_usuario)
        if not usuario:
            abort(404, message='id de Usuario no encontrado') 
        
        for key, value in user_data.__dict__.items():
            if key != 'id_usuario' and hasattr(usuario, key):
                setattr(usuario, key, value)

        try:
            db.session.commit()

        except IntegrityError as e:
            db.session.rollback()
            if 'correo' in str(e):
                abort(400, message='El correo esta registrado con otro usuario')
            raise e
        
        except SQLAlchemyError:
            db.session.rollback()
            abort(500, message="Error al actualizar el usuario")

        return usuario

# Endpoint para eliminar un usuario por su ID
@usuarios_bp.route('/usuarios/delete/<string:id_usuario>')
class UsuarioDelete(MethodView):
    @usuarios_bp.response(200, UsuarioSchema)
    def delete(self, id_usuario):
        """
        Elimina un usuario del sistema.

        :param id_usuario: El ID del usuario a eliminar.

        **Respuesta exitosa (200):**
        Devuelve los detalles del usuario eliminado.

        **Error 404:**
        Si no se encuentra el usuario con el `id_usuario` especificado.

        **Error 400:**
        Si ocurre un error al intentar eliminar el usuario en la base de datos.
        """
        usuario = Usuario.query.get_or_404(id_usuario)

        try:
            db.session.delete(usuario)
            db.session.commit()
        except SQLAlchemyError:
            abort(400, message='Error al borrar usuario')
        return usuario