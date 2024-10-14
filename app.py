from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy


with app.app_context():
    try:
        db.engine.execute("SELECT 1")
        print("si")
    except:
        print('no')

@app.route('/api/sensors')
def sensores():
    return jsonify(mesage='sensor')

@app.route('/api/cameras')
def camaras():
    return jsonify(message='camara')

@app.route("/api/users")
def users():
    return jsonify(message='users')

@app.route("/api/users/<string:id>")
def users_id(id: str):
    return jsonify(user=id)

@app.route('/api/alerts')
def alerts():
    return jsonify(message='alerts')

@app.route('/api/wifi')
def wifi():
    return jsonify(message='wifi')

@app.route('/api/not-found')
def not_found():
    return jsonify(message='request not found'), 404

if __name__ == '__main__':
    app.run(debug=True)


