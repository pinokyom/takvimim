from flask import Flask, request, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="Takvim", static_url_path="")
CORS(app)

# BURAYA Render'dan aldığın veritabanı bağlantısını yapıştır
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bl4ck:J4Qv9J7gfExZ0XSHPAuZa0vAWdU54te5@dpg-d3t8afp5pdvs73alt75g-a:5432/takvimdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), unique=True, nullable=False)
    note = db.Column(db.Text, nullable=True)
    done = db.Column(db.Boolean, default=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def index():
    return send_from_directory("Takvim", "index.html")

@app.route("/notes/<date>", methods=["GET", "POST", "DELETE"])
def notes(date):
    note_entry = Note.query.filter_by(date=date).first()

    if request.method == "GET":
        if note_entry:
            return jsonify({"note": note_entry.note, "done": note_entry.done})
        return jsonify({})

    elif request.method == "POST":
        data = request.json
        if note_entry:
            note_entry.note = data.get("note", "")
            note_entry.done = data.get("done", False)
        else:
            note_entry = Note(date=date, note=data.get("note", ""), done=data.get("done", False))
            db.session.add(note_entry)
        db.session.commit()
        return jsonify({"status": "saved"})

    elif request.method == "DELETE":
        if note_entry:
            db.session.delete(note_entry)
            db.session.commit()
        return jsonify({"status": "deleted"})

if __name__ == "__main__":
    app.run()
