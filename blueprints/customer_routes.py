
from flask import Blueprint, render_template, jsonify, request, session


customer = Blueprint("customer", __name__, template_folder="templates")

@customer.route("/api/user_info", methods=["GET"])
def user_info():
    if "user" not in session:
        print("User not logged in")
        print(session)
        return jsonify({"error": "User not logged in"}), 401

    user = session["user"]
    print(user)
    user_info = {
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "birthdate": user["birthdate"],
        "monthly_salary": user["monthly_salary"],
        "account_number": user["account_number"],
        "balance": user["balance"]
    }
    print("User info:", user_info)
    print("Sent user info to client")

    response = jsonify(user_info)
    return response, 200
