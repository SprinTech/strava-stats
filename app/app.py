from flask import Flask, render_template
from .config import config
from .routes.auth import bp as auth_bp
from .routes.users import bp as user_bp

app = Flask(__name__)
app.config.from_object(config["development"])
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)


@app.route("/")
def index():
    return render_template("dashboard.html")
