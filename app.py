from tomllib import load

from flask import Flask, redirect, render_template

app = Flask(__name__)

IP = "http://192.168.0.108"


@app.route("/")
def index():
    with open("site.toml", "rb") as f:
        tdata = load(f)
        data = [tdata.get(d) for d in tdata]
        for d in data:
            d["url"] = f"{IP}:{d['port']}"
    return render_template("index.html", sites=data)


@app.errorhandler(404)
def handle(e):
    return redirect("/")
