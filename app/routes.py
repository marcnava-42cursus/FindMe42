from flask import Flask, jsonify
from services.endpoints import get_user_data
from core import APIClient

app = Flask(__name__)

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user_data = get_user_data(user_id)
    if user_data is None:
        return jsonify({"error": "User data unavailable"}), 404
    return jsonify(user_data), 200

@app.route("/token", methods=["GET"])
def get_token():
    client = APIClient()
    return jsonify({"token": client.get_token()}), 200