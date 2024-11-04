from flask import Flask, render_template
from models import db
from schemas import ma
from routes import  register_blueprints
from flask_smorest import Api
from routes.usuarios_route import usuarios_bp
import os 



app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Roseta Inteligente API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config['OPENAPI_URL_PREFIX'] = '/'
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tester:test@localhost/test'



api = Api(app)
api.register_blueprint(usuarios_bp, url_prefix='/api')

@app.route('/')
def home():
    return render_template('index.html')


db.init_app(app)
ma.init_app(app)



#registrar blueprints
register_blueprints(api)


if __name__ == '__main__':
    app.run(debug=True)


