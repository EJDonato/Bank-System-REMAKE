
from flask import Blueprint, request, Response, render_template

from backend import CustomerFacade


signup_routes = Blueprint("signup_routes", __name__, template_folder="templates")

# Route for handling sign-up information 
@signup_routes.route("/sign_up_info", methods=["POST"])
def sign_up_info():
    data = request.form

    first_name = data.get("firstName")
    last_name = data.get("lastName")
    email = data.get("email")
    password = data.get("password")
    birthdate = data.get("bdate")
    monthly_salary = data.get("monthlySalary")
    bank_account_pin = data.get("pin")
    start_balance = data.get("startBalance")
    user_type = data.get("userType")

    facade = CustomerFacade()

    if facade.sign_up(email, password, first_name, last_name, birthdate, bank_account_pin, monthly_salary, start_balance, user_type):
        return Response(status=200)
    else:
        return Response(status=400)
    
@signup_routes.route("/sign_up/<user_type>")
def sign_up(user_type):
    print(user_type)
    return render_template("sign_up.html", user_type=user_type)