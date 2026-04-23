from flask import Flask, jsonify, request
from sql_storage import (
    init_db,
    get_all_notes_sql,
    create_note_sql,
    get_note_by_id_sql,
    update_note_sql,
    delete_note_sql,
)
from storage import (
    get_all_notes_json,
    create_note_json,
    get_note_by_id_json,
    update_note_json,
    delete_note_json
)

app = Flask(__name__)

SQL_MODE = True

def get_json_data():
    data = request.get_json()
    if data is None:
        return None, (jsonify({"error": "JSON is required"}), 400)
    return data, None

@app.route("/notes", methods=["GET"])
def get_notes():
    if SQL_MODE:
        notes = get_all_notes_sql()
    else:
        notes = get_all_notes_json()
    return jsonify(notes)

@app.route("/notes", methods=["POST"])
def create_note():
    data, error = get_json_data()
    if error:
        return error
    title = data.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400
    content = data.get("content")
    if SQL_MODE:
        note = create_note_sql(title, content)
    else:
        note = create_note_json(title, content)
    return jsonify(note), 201

@app.route("/notes/<int:note_id>", methods=["GET"])
def get_note(note_id):
    if SQL_MODE:
        note = get_note_by_id_sql(note_id)
    else:
        note = get_note_by_id_json(note_id)
    if note:
        return jsonify(note)
    return jsonify({"error": "Note not found"}), 404

@app.route("/notes/<int:note_id>", methods=["PUT"])
def update_note(note_id):
    data, error = get_json_data()
    if error:
        return error
    title = data.get("title")
    content = data.get("content")

    if SQL_MODE:
        note = update_note_sql(note_id, title, content)
    else:
        note = update_note_json(note_id, title, content)

    if not note:
        return jsonify({"error": "Note not found"}), 404

    return jsonify(note)

@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    if SQL_MODE:
        deleted = delete_note_sql(note_id)
    else:
        deleted = delete_note_json(note_id)
    if not deleted:
        return jsonify({"error": "Note not found"}), 404
    return jsonify({"message": "Note deleted"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5001)