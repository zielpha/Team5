import sqlite3
from datetime import datetime

# Function to connect to the database
def connect_db():
    return sqlite3.connect('notes.db')

# Function to add a note
def add_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO notes (title, content, created_at)
    VALUES (?, ?, ?)
    ''', (title, content, created_at))
    conn.commit()
    conn.close()
    print("Note added successfully!\n")

# Function to view all notes
def view_notes():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notes')
    notes = cursor.fetchall()
    conn.close()
    
    if not notes:
        print("No notes found.\n")
    else:
        print("\n--- Your Notes ---")
        for note in notes:
            print(f"ID: {note[0]}")
            print(f"Title: {note[1]}")
            print(f"Content: {note[2]}")
            print(f"Created At: {note[3]}\n")

# Function to update a note
def update_note():
    note_id = input("Enter the ID of the note to update: ")
    title = input("Enter new title (leave blank to keep current): ")
    content = input("Enter new content (leave blank to keep current): ")
    
    conn = connect_db()
    cursor = conn.cursor()
    
    if title or content:
        cursor.execute('''
        UPDATE notes
        SET title = COALESCE(?, title),
            content = COALESCE(?, content)
        WHERE id = ?
        ''', (title if title else None, content if content else None, note_id))
        conn.commit()
        print("Note updated successfully!\n" if cursor.rowcount > 0 else "No note found with that ID.\n")
    else:
        print("No changes made.\n")
    
    conn.close()

# Function to delete a note
def delete_note():
    note_id = input("Enter the ID of the note to delete: ")
    
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    conn.commit()
    print("Note deleted successfully!\n" if cursor.rowcount > 0 else "No note found with that ID.\n")
    conn.close()

# Main function
def main():
    while True:
        print("1. Add Note")
        print("2. View Notes")
        print("3. Update Note")
        print("4. Delete Note")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()