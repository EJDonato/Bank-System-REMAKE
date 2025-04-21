from flask import Flask, jsonify, render_template, request


class FlaskApp():
    def __init__(self):
        
        self.app = Flask(__name__)

        @self.app.route("/")
        def index():
            return render_template("index.html")