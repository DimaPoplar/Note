import json
import datetime


class Note:
    def __init__(self, id, title, body, created_date=None, updated_date=None):
        self.id = id
        self.title = title
        self.body = body
        self.created_date = created_date or datetime.datetime.now()
        self.updated_date = updated_date or self.created_date


class NotesManager:
    def __init__(self, filename):
        self.filename = filename
        self.notes = []

    def create_note(self):
        id = len(self.notes) + 1
        title = input("Enter note title: ")
        body = input("Enter note body: ")
        note = Note(id, title, body)
        self.notes.append(note)
        print("Note created successfully!")

    def read_notes(self):
        try:
            with open(self.filename, "r") as file:
                notes_data = json.load(file)
                self.notes = [Note(**note_data) for note_data in notes_data]
        except FileNotFoundError:
            print("No notes found.")

    def update_note(self):
        id = int(input("Enter note id: "))
        note = self._get_note_by_id(id)
        if note:
            title = input(f"Enter new title for note {id}: ")
            body = input(f"Enter new body for note {id}: ")
            note.title = title
            note.body = body
            note.updated_date = datetime.datetime.now()
            print("Note updated successfully!")
        else:
            print(f"Note {id} not found.")

    def delete_note(self):
        id = int(input("Enter note id: "))
        note = self._get_note_by_id(id)
        if note:
            self.notes.remove(note)
            print("Note deleted successfully!")
        else:
            print(f"Note {id} not found.")

    def save_notes(self):
        notes_data = [vars(note) for note in self.notes]
        with open(self.filename, "w") as file:
            json.dump(notes_data, file)

    def _get_note_by_id(self, id):
        for note in self.notes:
            if note.id == id:
                return note
        return None


def main():
    filename = "notes.json"
    manager = NotesManager(filename)
    manager.read_notes()

    while True:
        print("\n1. Create note")
        print("2. Read notes")
        print("3. Update note")
        print("4. Delete note")
        print("5. Save notes")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            manager.create_note()
        elif choice == "2":
            for note in manager.notes:
                print(f"{note.id}. {note.title}")
        elif choice == "3":
            manager.update_note()
        elif choice == "4":
            manager.delete_note()
        elif choice == "5":
            manager.save_notes()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()