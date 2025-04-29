from flask import Flask, jsonify, render_template, request

# test function only, delete later
def login_test(email, password):
    test_email = "airam@gmail.com"
    test_password = "abc123"

    if test_email == email and test_password == password:
        acc_name = "AiramJeanReglos"
        return [True, acc_name]
    else:
        return [False, "accNotFound"]

class FlaskApp():
    def __init__(self):
        
        self.app = Flask(__name__)

        @self.app.route("/")
        def index():
            return render_template("index.html")
        
        @self.app.route("/login")
        def login():
            return render_template("login.html")
        
        @self.app.route("/homepage/<user>")
        def homepage(user):
            return render_template("home_page.html")
        
        # this is where python fetches login info
        @self.app.route("/login/login_info", methods=["POST"])
        def check_login_info():
            data = request.json
            email = data.get("email")
            password = data.get("password")

            check = login_test(email, password)
            result = {"result":check[0],
                      "acc_name":check[1]}

            return jsonify(result)

        

    def run(self, **kwargs):
        self.app.run(**kwargs)


app = FlaskApp().app

if __name__ == "__main__":
    app.run(debug=True)



