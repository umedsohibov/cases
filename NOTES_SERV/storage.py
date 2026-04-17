import json
FILE_NAME =  "notes.json"
def load_notes():
    with open(FILE_NAME, "r") as file:
        return json.load(file)
def save_notes(notes):
    with open(FILE_NAME, "w") as file:
        json.dump(notes, file, indent=4)