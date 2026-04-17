import sqlite3 #modul
DB_NAME = "notes.db" #db name
def get_connection():# connection to db
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS notes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   content TEXT
                )
                   """)
    conn.commit()
    conn.close()

def get_all_notes_sql():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id,title,content FROM notes")
    rows = cursor.fetchall()
    conn.close()
    notes = []
    for row in rows:
        notes.append({"id": row[0], "title": row[1], "content": row[2]})
    return notes
def create_note_sql(title, content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes(title,content) VALUES(?,?)",
        (title,content)
    )
    note_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return {"id": note_id, "title": title, "content": content}
def get_note_by_id_sql(note_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, content FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"id": row[0], "title": row[1], "content": row[2]}
    return None
def update_note_sql(note_id, title, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, title, content FROM notes WHERE id = ?",
        (note_id,)
    )
    row = cursor.fetchone()

    if not row:
        conn.close()
        return None

    current_title = row[1]
    current_content = row[2]

    new_title = title if title is not None else current_title
    new_content = content if content is not None else current_content

    cursor.execute(
        "UPDATE notes SET title = ?, content = ? WHERE id = ?",
        (new_title, new_content, note_id)
    )

    conn.commit()
    conn.close()

    return {
        "id": note_id,
        "title": new_title,
        "content": new_content
    }
def delete_note_sql(note_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM notes WHERE id = ?", (note_id,))
    row = cursor.fetchone()

    if not row:
        conn.close()
        return False

    cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()

    return True