from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = "511f80f1f19a7615df742d2c12026014"

posts = [
    {
        "author" : "Corey Schafer",
        "title" : "Blog Post 1",
        "content" : "First Blog Post",
        "date_posted" : "April 20 2018"
    },
    {
        "author" : "Isaac Irungu",
        "title" : "Blog Post 2",
        "content" : "Second Blog Post",
        "date_posted" : "April 21 2018"
    }
]

@app.route("/about")
def about():
    return render_template('about.html', title = "About")

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts = posts)
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title = "Register", form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title = "Login", form = form)