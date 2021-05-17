from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Xinqui</h1><h2>Ningguang</h2>"

@app.route("/about")
def about():
    return "<h1>Diluc</h1><h2>Rosaria</h2>"

@app.route("/home")
def home():
    return "<h1>Sucrose</h1><h2>Come Home</h2>"

if __name__ == "__main__":
    app.run(debug=True)