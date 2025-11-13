from flask import Blueprint, jsonify
from .database import get_latest_readings

api = Blueprint('api', __name__)

@api.route('/readings', methods=['GET'])
def readings():
    data = get_latest_readings()
    return jsonify(data)

def create_app():
    from flask import Flask
    app = Flask(__name__)
    app.register_blueprint(api)
    return app
