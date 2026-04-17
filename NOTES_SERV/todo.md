1. Ввести sql mode
Пример работы:
global variable SQL_MODE=True | False

2. Динамически выбирать storage
Пример работы:
@app.route("/notes", methods=["POST"])
def create_note():
    if SQL_MODE:
        # save to sql
        note = create_note_sql()
    else:
        # save to json
        note = create_note_json()
    return jsonify(note), 201

def create_note_sql():
    return

def create_note_json():
    return

3. МЫ НЕ СИНХРОНИЗИРУЕМ БД ДРУГ С ДРУГОМ. У НАС МОЖЕТ БЫТЬ РАСХОЖДЕНИЕ В ДАННЫХ. ЭТО ОКЕЙ
4. Удалить комменты
5. Опционально - разобраться с docker и docker compose. Сделать Dockerfile + docker-compose.yml + заменить sqlite на postgres