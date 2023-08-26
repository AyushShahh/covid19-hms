import data as d
from flask import Flask, redirect, render_template, request, session


db = d.db()
hospitals = d.hospitals(db)
people = d.people(db)
medicines = d.medicines(db)
laboratory = d.laboratory(db)

# Initialize flask app
app = Flask(__name__)

# Index route with GET and POST methods
@app.route("/", methods=["GET", "POST"])
def index():

    # When user reaches the page via post i.e., submitting the form
    if request.method == "POST":
        city = request.form.get("city").lower()
        return render_template("index.html", data=[item for item in hospitals if item == city], show=True)
    else:
        return render_template("index.html")