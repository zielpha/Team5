import sqlite3
from datetime import datetime

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('notes.db')
cursor = conn.cursor()

# Create the notes table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT NOT NULL
)
''')
conn.commit()

def add_note():
    """Add a new note to the database."""
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute('''
    INSERT INTO notes (title, content, created_at)
    VALUES (?, ?, ?)
    ''', (title, content, created_at))
    conn.commit()
    print("Note added successfully!\n")

def view_notes():
    """View all notes in the database."""
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    
    if not notes:
        print("No notes found.\n")
    else:
        print("\n--- Your Notes ---")
        for note in notes:
            print(f"ID: {note[0]}")
            print(f"Title: {note[1]}")
            print(f"Content: {note[2]}")
            print(f"Created At: {note[3]}\n")

def delete_note():
    """Delete a note by its ID."""
    note_id = input("Enter the ID of the note to delete: ")
    
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    print("Note deleted successfully!\n" if cursor.rowcount > 0 else "No note found with that ID.\n")

def main():
    """Main function to run the note-taking app."""
    while True:
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

# Close the database connection when done
conn.close()