from flask import Flask, request, render_template, jsonify
import base64

app = Flask(__name__)

# Store latest data
latest_data = {"detections": [], "frame": None}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    global latest_data
    data = request.get_json()
    latest_data["detections"] = data["detections"]
    latest_data["frame"] = data["frame"]
    return jsonify({"status": "success"})

@app.route("/stream")
def stream():
    frame = latest_data["frame"]
    if frame:
        return f"data:image/jpeg;base64,{frame}"
    return ""

@app.route("/detections")
def get_detections():
    return jsonify(latest_data["detections"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)