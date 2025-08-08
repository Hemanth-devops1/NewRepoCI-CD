from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)

@bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK", "message": "This is my app"}), 200
