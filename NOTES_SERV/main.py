from flask import Flask, jsonify, request #Flask это сервер, jsonify - чтоб json работали, request - читать запросы.
#from storage import load_notes, save_notes
from sql_storage import init_db
from sql_storage import get_all_notes_sql
from sql_storage import create_note_sql
from sql_storage import get_note_by_id_sql
from sql_storage import update_note_sql
from sql_storage import delete_note_sql

app = Flask(__name__) # Создаем приложение
#notes= load_notes()
#if notes:
#    next_id = max(note["id"] for note in notes) + 1
#else:
#    next_id = 1

def get_json_data(): #выводим ошибки чтоб не дублировались
    data = request.get_json()
    if data is None:
       return None, (jsonify({"error":"JSON is required"}), 400 )
    return data, None
#def find_note_by_id(note_id):
    for note in notes:
        if note["id"] == note_id:
            return note
    return None

@app.route("/notes", methods=["GET"]) #если придёт GET-запрос на /notes, выполнить
def get_notes(): # функция
    return jsonify(get_all_notes_sql()) # возвращаем список заметок/ SQL ADD
@app.route("/notes", methods=["POST"])
def create_note():
   # global next_id
    data, error = get_json_data()
    if error:
        return error
    title = data.get("title") # Можно было сделать data ["title"], но лучше .get() при отсутствии ключа не выпадет в ошибку, а вернет None
    if not title:
        return jsonify({"error":"Title is required"}), 400
    content = data.get("content")
    note = create_note_sql(title, content) #{
        #"id": next_id,
       # "title": title,
       # "content": content
    #}
    #notes.append(note)
    #save_notes(notes) #выгружаем из storage
    #next_id += 1
    return jsonify(note), 201
@app.route("/notes/<int:note_id>", methods=["GET"]) # каждому json присваеваем страницу одна заметка по id
def get_note(note_id):
    note = get_note_by_id_sql(note_id)
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

    note = update_note_sql(note_id, title, content)

    if not note:
        return jsonify({"error": "Note not found"}), 404

    return jsonify(note)
    #note = find_note_by_id(note_id)
    #if not note:
     #   return jsonify({"error": "Note not found"}), 404
    #title = data.get("title")
    #content = data.get("content")
    #if title:
    #    note["title"] = title
#
 #   if content:
  #        note["content"] = content
   # save_notes(notes) #обновить из storage
    #return jsonify(note)

@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    deleted = delete_note_sql(note_id)
    if not deleted:
        return jsonify({"error": "Note not found"}), 404
   # note = find_note_by_id(note_id)
    #if not note:
     #   return jsonify({"error": "Note not found"}), 404
    #notes.remove(note)
    #save_notes(notes)
    return jsonify({"message": "Note deleted"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True, port = 5001) # start server пришлось сменить порт 5000 чем-то забил