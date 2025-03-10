import http.server
import json
import sqlite3
from urllib.parse import parse_qs

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect("notes.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

class NotesHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/notes":
            self.get_notes()
        else:
            super().do_GET()
    
    def do_POST(self):
        if self.path == "/add":
            self.add_note()
        elif self.path == "/update":
            self.update_note()
        elif self.path == "/delete":
            self.delete_note()
    
    def get_notes(self):
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes")
        notes = [{"id": row[0], "content": row[1]} for row in cursor.fetchall()]
        conn.close()
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(notes).encode())
    
    def add_note(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notes (content) VALUES (?)", (data["content"],))
        conn.commit()
        conn.close()
        
        self.send_response(201)
        self.end_headers()
    
    def update_note(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE notes SET content = ? WHERE id = ?", (data["content"], data["id"]))
        conn.commit()
        conn.close()
        
        self.send_response(200)
        self.end_headers()
    
    def delete_note(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        
        conn = sqlite3.connect("notes.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM notes WHERE id = ?", (data["id"],))
        conn.commit()
        conn.close()
        
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    init_db()
    server = http.server.HTTPServer(("", 8000), NotesHandler)
    print("Server running on port 8000...")
    server.serve_forever()
