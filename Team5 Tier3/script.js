document.addEventListener("DOMContentLoaded", loadNotes);

function loadNotes() {
    fetch("/notes")
        .then(response => response.json())
        .then(data => {
            console.log("Fetched Notes:", data); // Debugging
            const notesList = document.getElementById("notesList");
            notesList.innerHTML = "";
            data.forEach(note => {
                let li = document.createElement("li");
                li.textContent = `ID: ${note.id} - ${note.content}`;
                notesList.appendChild(li);
            });
        })
        .catch(error => console.error("Error fetching notes:", error));
}

function addNote() {
    const content = document.getElementById("noteContent").value;
    fetch("/add", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ content })
    }).then(() => {
        document.getElementById("noteContent").value = "";
        loadNotes();
    });
}

function updateNote() {
    const id = document.getElementById("updateId").value;
    const content = document.getElementById("updateContent").value;
    fetch("/update", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, content })
    }).then(() => {
        document.getElementById("updateId").value = "";
        document.getElementById("updateContent").value = "";
        loadNotes();
    });
}

function deleteNote() {
    const id = document.getElementById("deleteId").value;
    fetch("/delete", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id })
    }).then(() => {
        document.getElementById("deleteId").value = "";
        loadNotes();
    });
}
