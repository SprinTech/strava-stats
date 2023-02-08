from flask import Flask
from .config import config

app = Flask(__name__)
app.config.from_object(config["development"])


@app.route("/")
def index():
    return {"message": "Hello World !"}
