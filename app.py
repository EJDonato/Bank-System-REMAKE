from flask import Flask, jsonify, render_template, request
from blueprints.customer_routes import customer

class FlaskApp():
    def __init__(self):
        
        self.app = Flask(__name__)
        self.app.register_blueprint(customer)

        @self.app.route("/")
        def index():
            return render_template("index.html")
        
        @self.app.route("/sign_up")
        def sign_up():
            return render_template("sign_up.html")
        
        @self.app.route("/pending_account")
        def pending_account():
            return render_template("pending_account_page.html")
        

    def run(self, **kwargs):
        self.app.run(**kwargs)


app = FlaskApp().app

if __name__ == "__main__":
    app.run(debug=True)



