
from flask import Blueprint, render_template, jsonify, request


customer = Blueprint("customer", __name__, template_folder="templates")

@customer.route("/homepage/<user>")
def homepage(user):
    return render_template("home_page.html")


