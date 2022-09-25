from flask import render_template,Flask,redirect,request
from database import Database
from flask_session import Session


app = Flask(__name__)

post_template = {
    "Title":"",
    "Description":"",
    "upvotes":0,
    "downvotes":0,
    "tags":[]
}
@app.route("/")
def red():
    return redirect("/index")


@app.route("/index")
def main():
    return render_template("index.html")

@app.route("/step1")
def s1():
    return render_template("step1.html")

@app.route("/googlemaps")
def s2():
    return render_template("googlemaps.html")
@app.route("/feed")
def s3():
    return render_template("feed.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
