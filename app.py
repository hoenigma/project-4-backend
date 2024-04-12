# save this as app.py
from flask import Flask

# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# import marshmallow
from flask_marshmallow import Marshmallow

# import bcrypt
from flask_bcrypt import Bcrypt

# import the uri
from config.environment import db_URI

app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!"


# Added this configuration
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI

#  Instatiate the SQLAlchemy class
db = SQLAlchemy(app)

# Instantiate Marshmalllow to tell it about Flask (like the above fro SQLA)
marsh = Marshmallow(app)

# ! Create bcrypt plugin, tell it about flask
bcrypt = Bcrypt(app)

# Routes for the controllers
# from controllers import users

# app.register_blueprint(users.router, url_prefix="/api")
