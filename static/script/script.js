function logout() {
    if (confirm('Are you sure you want to logout?')) {
        window.location.href = '/logout';
    }
}

function deleteNote() {
    return confirm('Are you sure you want to delete this note?');
}

function greetTimeOfDay() {
    // get local of the user
    const date = new Date();
    const hour = date.getHours();
    let greeting = '';
    // morning and evening only
    if (hour >= 0 && hour < 12) {
        greeting = '☀️ Good day';
    } else if (hour < 18) {
        greeting = '🌙 Good evening';
    }
    return greeting;
}