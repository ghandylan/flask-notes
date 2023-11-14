function logout() {
    if (confirm('Are you sure you want to logout?')) {
        window.location.href = '/logout';
    }
}

function deleteNote() {
    return confirm('Are you sure you want to delete this note?');
}
