from flask import Flask, jsonify, render_template, request, redirect, Response, session
from flask_cors import CORS
import secrets

from blueprints import customer, login_routes, signup_routes


class FlaskApp():
    def __init__(self):
        
        self.app = Flask(__name__)
        
        # Register blueprints
        for blueprint in [customer, login_routes, signup_routes]:
            self.app.register_blueprint(blueprint)

        CORS(self.app, supports_credentials=True, resources={r"/api/*": {"origins": "http://localhost:5173"}})  # Allow CORS for the frontend
        self.app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)

        self.app.secret_key = "super_secret_key"  # Generate a random secret key for session management
        
        @self.app.route("/logout", methods=["POST"])
        def logout():
            session.clear()
            return Response(status=200)
           

    def run(self, **kwargs):
        self.app.run(**kwargs)


app = FlaskApp().app

if __name__ == "__main__":
    app.run(debug=True)



