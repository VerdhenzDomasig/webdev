from flask import Flask, render_template

from works import register_works_routes
from works.binary_tree import register_binary_tree_routes

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


register_works_routes(app)
register_binary_tree_routes(app)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
