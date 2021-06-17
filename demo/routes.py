from demo import app
from flask import jsonify


@app.route("/")
def _get_root():
    return jsonify({"status": "ok"}), 200
