from flask import Blueprint, jsonify

routes = Blueprint('routes', __name__)

@routes.route("/health")
def health():
    return jsonify({"status": "ok"})

@routes.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ])