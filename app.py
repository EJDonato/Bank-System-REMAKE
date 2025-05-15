from flask import Flask, jsonify, render_template, request

from blueprints.customer_routes import customer
from backend.customer_scripts import CustomerFacade

CustomerFacade()

class FlaskApp():
    def __init__(self):
        
        self.app = Flask(__name__)
        self.app.register_blueprint(customer)
        self.app.secret_key = "f3a8c91e1c9d4b9a84a7b6cd9a5db57e"

        @self.app.route("/")
        def index():
            return render_template("index.html")
        
        @self.app.route("/sign_up/<user_type>")
        def sign_up(user_type):
            print(user_type)
            return render_template("sign_up.html", user_type=user_type)
        
        @self.app.route("/pending_account")
        def pending_account():
            return render_template("pending_account_page.html")
        
        @self.app.route("/login_info", methods=["POST"])
        def login():
            data = request.json
            email = data.get("email")
            password = data.get("password")

            facade = CustomerFacade()

            success = facade.log_in(email, password) 

            if not success:
                return False
            else:
                return success
            
        @self.app.route("/sign_up_info", methods=["POST"])
        def sign_up_info():
            data = request.json

            first_name = data.get("first_name")
            last_name = data.get("last_name")
            email = data.get("email")
            password = data.get("password")
            birthdate = data.get("bdate")
            monthly_salary = data.get("monthly_salary")
            bank_account_pin = data.get("pin")
            start_balance = data.get("start_balance")
            user_type = data.get("user_type")

            print(bank_account_pin)

            facade = CustomerFacade()

            facade.sign_up(email, password, first_name, last_name, birthdate, bank_account_pin, monthly_salary, start_balance, user_type)

        

    def run(self, **kwargs):
        self.app.run(**kwargs)


app = FlaskApp().app

if __name__ == "__main__":
    app.run(debug=True)



