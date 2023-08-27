import data as d
from flask import Flask, redirect, render_template, request


db = d.db()
hospitals = d.hospitals(db)
people = d.people(db)
medicines = d.medicines(db)
laboratory = d.laboratory(db)


app = Flask(__name__)

def update():
    global hospitals
    global people
    global medicines
    global laboratory
    hospitals = d.hospitals(db)
    people = d.people(db)
    medicines = d.medicines(db)
    laboratory = d.laboratory(db)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city").lower()
        condition = request.form.get("condition").lower()
        update()
        return render_template("index.html", data=[item for item in hospitals if item[11] == city and (item[7] > 0 if condition == 'severe' else True)], show=True)
    else:
        return render_template("index.html")
    
@app.route("/hospitals", methods=["GET", "POST"])
def hospital():
    if request.method == "POST":
        hospital_id = int(request.form.get("id"))
        t_nbeds = int(request.form.get("t_nbeds")) if request.form.get("t_nbeds") else 0
        a_nbeds = int(request.form.get("a_nbeds")) if request.form.get("a_nbeds") else 0
        t_vbeds = int(request.form.get("t_vbeds")) if request.form.get("t_vbeds") else 0
        a_vbeds = int(request.form.get("a_vbeds")) if request.form.get("a_vbeds") else 0
        staff = int(request.form.get("staff")) if request.form.get("staff") else 0
        oxygen = int(request.form.get("oxygen")) if request.form.get("oxygen") else 0
        nebulizer = int(request.form.get("nebulizer")) if request.form.get("nebulizer") else 0
        d.update_hospital(db, hospital_id, t_nbeds, a_nbeds, t_vbeds, a_vbeds, staff, oxygen, nebulizer)
        update()

        chospital = [hospital for hospital in hospitals if hospital[0] == hospital_id]
        if chospital:
            return render_template("hospital.html", data=chospital[0], show=True)
        else:
            return redirect("hospital.html")
    else:
        return render_template("hospital.html")

@app.route("/medicines", methods=["GET", "POST"])
def medic():
    if request.method == "POST":
        city = request.form.get("city").lower()
        d = [medicine for medicine in medicines if medicine[2] == city]
        show = True if d else False
        return render_template("medicine.html", data=d, show=show)
    else:
        return render_template("medicine.html")