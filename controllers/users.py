from http import HTTPStatus
from datetime import datetime, timedelta, timezone
import pytz
import jwt
from flask import Blueprint, request, jsonify, g
from marshmallow.exceptions import ValidationError
from config.environment import SECRET
from app import db
from models.user import UserModel
from middleware.secure_route import secure_route

# from models.user import UserModel
from serializers.user import UserSerializer

user_serializer = UserSerializer()

router = Blueprint("users", __name__)


# sign up user
@router.route("/signup", methods=["POST"])
def signup():

    try:
        user_dictionary = request.json
        # have to give them role of 1 (user)
        user_dictionary["roles"] = 1
        # user_dictionary["favourite_region"] = None

        print(user_dictionary)

        user_model = user_serializer.load(user_dictionary)

        # db.session.add(user_model)
        # db.session.commit()
        user_model.save()

        print("user model", user_model.password)

        return user_serializer.jsonify(user_model)
    except ValidationError as e:
        return {
            "errors": e.messages,
            "message": "Something went wrong",
        }, HTTPStatus.UNPROCESSABLE_ENTITY
    except Exception as e:
        print(e)
        return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR


@router.route("/login", methods=["POST"])
def login():
    try:
        # If user is who they say they are, send back JWT

        # Get the info
        credentials_dictionary = request.json

        # print("This is ", credentials_dictionary)

        # Get user from database
        user = (
            db.session.query(UserModel)
            .filter_by(email=credentials_dictionary["email"])
            .first()
        )

        print("user...", user)
        # No user
        if not user:
            return {"message": "Login failed. Try again."}, 401
        # Comapre the two hashed password together
        if not user.validate_password(credentials_dictionary["password"]):
            return {"message": "Login failed. Try again."}, 401

        # print("otherwise success!!")
        # return {"message": "yaaaayyyy"}
        # generate JWT Token
        payload = {
            "exp": datetime.now(timezone.utc) + (timedelta(days=1)),  # Expiry date
            "iat": datetime.now(pytz.UTC),
            "sub": user.id,  # User.id as sub
        }
        print(payload["exp"])
        print(payload["iat"])

        token = jwt.encode(payload, SECRET, algorithm="HS256")

        # Return success message along with JWT token
        return {"message": "Login successful.", "token": token}
    except Exception as e:
        return {
            "message": "An error occurred while processing your request.",
            "error": str(e),
        }, 500


# get a user
@router.route("/user", methods=["GET"])
@secure_route
def get_single_user():
    try:
        # get the id from the user
        current_userId = g.current_user.id
        print("The current userID is ", current_userId)

        user = db.session.query(UserModel).get(current_userId)
        return user_serializer.jsonify(user)

    except ValidationError as e:
        return jsonify({"message": "something went wrong", "error": e.messages}), 422
    except Exception as e:
        return jsonify({"message": "Failed to fetch the user", "error": str(e)}), 500


# update user
@router.route("/user", methods=["PUT"])
@secure_route
def update_user():
    try:
        # get the id from the user
        current_userId = g.current_user.id
        print("The current userID is ", current_userId)

        existing_user = db.session.query(UserModel).get(current_userId)
        print(existing_user)

        data = request.json
        user = user_serializer.load(
            data,
            instance=existing_user,
            partial=True,
        )

        # save user
        user.save()
        return user_serializer.jsonify(user)

    except ValidationError as e:
        return (
            jsonify(
                {"message": "something went wrong in validation", "error": e.messages}
            ),
            422,
        )
    except Exception as e:
        print(e)
        return jsonify({"message": "something went wrong"}), 500


# delete user
@router.route("/user", methods=["DELETE"])
@secure_route
def delete_user():
    try:
        # get the id from the user
        current_userId = g.current_user.id
        print("The current userID is ", current_userId)

        user = db.session.query(UserModel).get(current_userId)
        print(user)

        db.session.delete(user)
        db.session.commit()
        return user_serializer.jsonify(user)

    except Exception as e:
        # If an error occurs, rollback the session and return an error response
        db.session.rollback()
        return jsonify({"message": "Failed to delete user", "error": str(e)}), 500
