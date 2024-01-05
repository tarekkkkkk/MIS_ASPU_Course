from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user credentials
valid_username = "user123"
valid_password = "password123"


@app.route("/")
def login_page():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username, password)
    if username == valid_username and password == valid_password:
        return "Login successful"
    else:
        return "Invalid credentials"


if __name__ == "__main__":
    app.run(debug=True)
