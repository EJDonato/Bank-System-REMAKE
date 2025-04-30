from flask import Flask, jsonify, render_template, request


class FlaskApp():
    def __init__(self):
        
        self.app = Flask(__name__)

        @self.app.route("/")
        def index():
            return render_template("index.html")
        

        @self.app.route("/homepage/<user>")
        def homepage(user):
            return render_template("home_page.html")
        

    def run(self, **kwargs):
        self.app.run(**kwargs)


app = FlaskApp().app

if __name__ == "__main__":
    app.run(debug=True)



