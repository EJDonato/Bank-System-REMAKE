
from flask import Blueprint, render_template, jsonify, request
from backend.customer_scripts.Login import Login

customer = Blueprint("customer", __name__, template_folder="templates")

@customer.route("/homepage/<user>")
def homepage(user):
    return render_template("home_page.html")

# DIPA TAPOS
@customer.route("/customer_login")
def customer_login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    check = Login(email, password)
    verify = check.check_account()

    