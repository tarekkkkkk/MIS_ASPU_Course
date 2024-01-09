// Optional validation using JavaScript
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const email = document.getElementById('email').value;
        const phone = document.getElementById('phone').value;

        if (!validateUsername(username) || !validatePassword(password) || !validateEmail(email) || !validatePhone(phone)) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });

    function validateUsername(username) {
        // Implement your username validation logic
        return true;
    }

    function validatePassword(password) {
        // Implement your password validation logic
        return true;
    }

    function validateEmail(email) {
        // Implement your email validation logic
        return true;
    }

    function validatePhone(phone) {
        // Implement your phone validation logic
        return true;
    }
});