
from flask import Blueprint, jsonify, request, session

from backend import CustomerFacade


login_routes = Blueprint("login_routes", __name__, template_folder="templates")

# Route for handling login information
@login_routes.route("/login_info", methods=["POST"])
def login():
    data = request.form
    email = data.get("email")
    password = data.get("password")
    user_type = data.get("userType")

    facade = CustomerFacade()

    user_info = facade.log_in(email, password, user_type) # This should get "pending" or "locked" or acc_num
    print(user_info)

    if user_info is None: # means user not found
        print("user info:", user_info)
        return jsonify({"error": "Invalid email or password"}), 404

    if user_info["status"] == "pending":
        return jsonify({"redirect_url": "/pending_account"})
    elif user_info["status"] == "locked":
        pass
    else: # means acc is active
        session["user"] = user_info
        print("User is now in session")
        return jsonify({"redirect_url": f"/homepage/{user_type}/{user_info['first_name'] + '-' + user_info['last_name']}"}), 200
