from flask import Flask, render_template,redirect
from models import db
from schemas import ma
from routes import  register_blueprints
from flask_smorest import Api
from routes.usuarios_route import usuarios_bp
import os 
from sqlalchemy import text

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Roseta Inteligente API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

db_uri = os.environ.get('POSTGRES_URL', 'postgresql://tester:test@localhost/test')

# Corrige el prefijo de la URI si es necesario
if db_uri.startswith("postgres://"):
    db_uri = db_uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/test-db-connection')
def test_db_connection():
    try:
        # Ejecuta una consulta simple para probar la conexión
        result = db.session.execute(text("SELECT 1"))
        return "Conexión exitosa a la base de datos", 200
    except Exception as e:
        return f"Error de conexión: {e}", 500

api = Api(app)
api.register_blueprint(usuarios_bp, url_prefix='/api')



db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()


#registrar blueprints
register_blueprints(api)


@app.route('/')
def home():
    return redirect('/swagger-ui')

if __name__ == '__main__':
    app.run(debug=True)


