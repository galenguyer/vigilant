from vigilant import app, get_stream, get_status
from flask import jsonify, Response, render_template


@app.route("/", methods=["GET"])
def _get_root():
    return render_template("index.html", status=get_status())

@app.route("/api/v1/stream", methods=["GET"])
def _get_api_v1_stream():
    return Response(get_stream(), mimetype="text/event-stream"), 200
