from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
# from forms import RegistrationForm, LoginForm

from datetime import datetime
app = Flask(__name__)

app.config['SECRET_KEY'] = "511f80f1f19a7615df742d2c12026014"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    img_file = db.Column(db.String(20), nullable = False, default = "default.jpeg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref = "author", lazy = True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}',  '{self.img_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

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