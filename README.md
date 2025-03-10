# Team5
1. Summary

This project explores three different database architectures using SQLite and Python:

1. Single-Tier Architecture

A standalone Python script that interacts with an SQLite database for a personal note-taking app.

Supports CRUD (Create, Read, Update, Delete) operations locally.

2. Two-Tier Architecture

Uses SQLite instead of MySQL to simulate a two-tier architecture.

The Python client script connects to the SQLite database and performs CRUD operations.

Suitable for client-server-based applications.

3. Three-Tier Architecture

Implements a web-based interface using Python (server), SQLite (database), and HTML/CSS/JavaScript (frontend).

A Python application server handles API requests to interact with the SQLite database.

Users can add, view, update, and delete notes through a simple web interface.

2. Running the Code

Single-Tier Architecture

1. Navigate to the single_tier/ directory.

2. Run the script:

python notes_db.py

3. Follow the on-screen prompts to add, view, update, or delete notes.

Two-Tier Architecture

1. Navigate to the two_tier/ directory.

2. Run the client script:

python client.py

3. The script will connect to the SQLite database and allow CRUD operations.

Three-Tier Architecture

1. Navigate to the three_tier/ directory.

2. Start the Python server:

python server.py

3. Open a browser and go to http://localhost:8000 to use the web interface.
