from flask import Flask, jsonify, render_template, request, redirect, Response, session
from flask_cors import CORS
import secrets

from blueprints import customer, login_routes, signup_routes


class FlaskApp():
    def __init__(self):
        
        self.app = Flask(__name__)
        CORS(self.app, supports_credentials=True)

        
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
        
        @self.app.route("/logout", methods=["POST"])
        def logout():
            session.clear()
            return Response(status=200)
           

    def run(self, **kwargs):
        self.app.run(**kwargs)


app = FlaskApp().app

if __name__ == "__main__":
    app.run(debug=True)



