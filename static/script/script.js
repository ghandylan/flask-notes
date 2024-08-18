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
    let greeting = 'Good';

    if (hour >= 0 && hour < 12) {
        greeting += ' morning';
    }
    else if (hour >= 12 && hour < 18) {
        greeting += ' afternoon';
    }
    else {
        greeting += ' evening';
    }
    return greeting;
}