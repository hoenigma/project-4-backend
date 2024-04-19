# save this as app.py
from flask import Flask

# import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# import marshmallow
from flask_marshmallow import Marshmallow

# import bcrypt
from flask_bcrypt import Bcrypt

# import CORS (for deployment)
from flask_cors import CORS

# import the uri
from config.environment import db_URI


app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello, World!"


# Added this configuration
app.config["SQLALCHEMY_DATABASE_URI"] = db_URI

# Add CORS
CORS(app)

#  Instatiate the SQLAlchemy class
db = SQLAlchemy(app)

# Instantiate Marshmalllow to tell it about Flask (like the above fro SQLA)
marsh = Marshmallow(app)

# ! Create bcrypt plugin, tell it about flask
bcrypt = Bcrypt(app)

# Routes for the controllers
from controllers import users
from controllers import projects
from controllers import regions

app.register_blueprint(users.router, url_prefix="/api")
app.register_blueprint(projects.router, url_prefix="/api")
app.register_blueprint(regions.router, url_prefix="/api")
