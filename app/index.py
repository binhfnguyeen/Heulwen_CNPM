from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta
app = Flask(__name__)
app.config["SECRET_KEY"] = "nguyendeptrai"
app.permanent_session_lifetime = timedelta(minutes=1)
@app.route('/')
def index():
    return render_template("colors.html")

@app.route('/user')
def hello_user():
    if "user" in session:
        name = session["user"]
        return f"<h1>Hello {name}<h1/>"
    else:
        return  redirect(url_for("login"))

@app.route('/colors/')
def colors():
    return render_template("colors.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        session.permanent = True # Neu khong tuong tac web 1 phut se bi out ra
        if user_name:
            session["user"]= user_name
            return redirect(url_for("hello_user", name=user_name))
        if "user" in session:
            name = session["user"]
            return f"<h1>Hello {name}<h1/>"
    return render_template("home.html")

@app.route("/logout")
def log_out():
    session.pop("user", None)
    return  redirect(url_for("login"))
if __name__ == '__main__':
    app.run(debug=True)