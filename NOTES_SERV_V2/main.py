from flask import Flask, jsonify, request

import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="notes_db",
        user="workbook1",
        password="",
        host="localhost",
        port="5432"
    )

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "ok"})

@app.route('/notes')
def get_notes():
    return jsonify([])

@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()

    title = data.get('title')
    content = data.get('content')

    return jsonify({
        "title": title,
        "content": content
    }), 201





@app.route("/db-test")
def db_test():
    conn = get_connection()
    conn.close()
    return jsonify({"db": "connected"})



if __name__ == "__main__":
    app.run(debug=True, port=5002)
