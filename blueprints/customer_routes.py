
from flask import Blueprint, render_template, jsonify, request


customer = Blueprint("customer", __name__, template_folder="templates")

@customer.route("/homepage/<user>")
def homepage(user):
    return render_template("home_page.html")


@customer.route("/homepage/<user>/deposit")
def deposit(user):
    return render_template("deposit.html")

@customer.route("/homepage/<user>/use_atm")
def use_atm(user):
    return render_template("use_atm.html")