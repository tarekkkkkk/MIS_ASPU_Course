<?php
// Optional server-side validation and user registration logic
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $email = $_POST["email"];
    $phone = $_POST["phone"];

    // Implement your registration logic here
    // You can validate the inputs, store the user details in a database, etc.

    // Example: Register the user and store the details in a file
    $userDetails = "Username: $username\nPassword: $password\nEmail: $email\nPhone: $phone\n";
    file_put_contents("users.txt", $userDetails, FILE_APPEND);

    echo "Registration successful. You can now log in with your username and password.";
}
?>