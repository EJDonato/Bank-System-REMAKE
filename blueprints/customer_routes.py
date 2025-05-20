
from flask import Blueprint, render_template, jsonify, request, session


customer = Blueprint("customer", __name__, template_folder="templates")

@customer.route("/homepage/customer/<user>")
def homepage(user):
    full_name = session["user"]["first_name"] + " " + session["user"]["last_name"]
    account_number = session["user"]["account_number"]
    balance = session["user"]["balance"]

    return render_template("home_page.html", full_name=full_name, acc_num=account_number, balance=balance)


@customer.route("/homepage/<user>/deposit")
def deposit(user):
    return render_template("deposit.html")


@customer.route("/homepage/<user>/use_atm")
def use_atm(user):
    return render_template("use_atm.html")