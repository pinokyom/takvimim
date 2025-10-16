from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "events.json"

def load_events():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_events(events):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, ensure_ascii=False, indent=2)

@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(load_events())

@app.route("/events", methods=["POST"])
def add_event():
    data = request.json
    events = load_events()
    events.append(data)
    save_events(events)
    return jsonify({"status": "ok", "event": data})

if __name__ == "__main__":
    app.run(debug=True)
