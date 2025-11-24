from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

logs = []


@app.route("/")
def home():
    return """
    <h2>Safe C2 Server</h2>
    <p>Use /receive to collect data</p>
    <p>Use /logs to view logs</p>
    """


@app.route("/receive", methods=["POST"])
def receive_data():
    try:
        data = request.json
        logs.append({
            "time": str(datetime.now()),
            "data": data
        })
        return jsonify({"status": "received"})
    except:
        return jsonify({"status": "error"})


@app.route("/logs")
def show_logs():
    html = "<h2>Received Logs</h2><hr>"
    for item in logs:
        html += f"<p><b>{item['time']}</b><br>{item['data']}<br><hr></p>"
    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
