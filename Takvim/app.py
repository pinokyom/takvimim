from flask import Flask, request, jsonify, send_from_directory
import json
import os

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bl4ck:J4Qv9J7gfExZ0XSHPAuZa0vAWdU54te5@dpg-d3t8afp5pdvs73alt75g-a:5432/takvimdb'


app = Flask(__name__, static_folder=".", static_url_path="")
DATA_FILE = "events.json"

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

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
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

