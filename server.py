from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store logs in memory
logs = []


@app.route("/")
def home():
    return """
    <h2>Safe C2 Server</h2>
    <p>POST data to <b>/receive</b></p>
    <p>View saved logs at <b>/logs</b></p>
    """


@app.route("/receive", methods=["POST"])
def receive_data():
    try:
        data = request.get_json(force=True, silent=True)
        logs.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "data": data
        })
        return jsonify({"status": True, "message": "Data received"})
    except Exception as e:
        return jsonify({"status": False, "error": str(e)})


@app.route("/logs", methods=["GET"])
def show_logs():
    html = "<h2>Received Logs</h2><hr>"

    for item in logs:
        html += f"""
        <p><b>{item['time']}</b><br>
        {item['data']}
        <br><hr></p>
        """

    return html


if __name__ == "__main__":
    # Render ignores this, but useful for local testing
    app.run(host="0.0.0.0", port=5000)
