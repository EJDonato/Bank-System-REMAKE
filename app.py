from flask import Flask, jsonify, render_template, request, redirect, Response, session
import secrets

from blueprints import customer, login_routes, signup_routes


class FlaskApp():
    def __init__(self):
        
        self.app = Flask(__name__)

        # Register blueprints
        for blueprint in [customer, login_routes, signup_routes]:
            self.app.register_blueprint(blueprint)

        self.app.secret_key = secrets.token_hex(16)  # Generate a random secret key for session management

        @self.app.route("/")
        def index():
            if "user" in session:
                return redirect(f"/homepage/customer/{session['user']['first_name'] + '-' + session['user']['last_name']}")

            return render_template("index.html", error_login=False)
        
        @self.app.route("/pending_account")
        def pending_account():
            return render_template("pending_account_page.html")
           

    def run(self, **kwargs):
        self.app.run(**kwargs)


app = FlaskApp().app

if __name__ == "__main__":
    app.run(debug=True)



