import json
FILE_NAME =  "notes.json"
def load_notes():
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)

def get_all_notes_json():
    return load_notes()

def create_note_json(title, content):
    notes = load_notes()
    if notes:
        next_id = max(note["id"] for note in notes) + 1
    else:
        next_id = 1

    note = {
        "id": next_id,
        "title": title,
        "content": content
    }
    notes.append(note)
    save_notes(notes)
    return note

def get_note_by_id_json(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            return note
    return None

def update_note_json(note_id, title, content):
    notes = load_notes()

    for note in notes:
        if note["id"] == note_id:
            if title is not None:
                note["title"] = title
            if content is not None:
                note["content"] = content

            save_notes(notes)
            return note
    return None

def delete_note_json(note_id):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_notes(notes)
            return True
    return False
