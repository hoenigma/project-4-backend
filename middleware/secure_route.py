from functools import wraps
from http import HTTPStatus
from flask import request, g
import jwt

from app import db
from models.user import UserModel

from config.environment import SECRET


def secure_route(
    route_func,
):  # This is a callback function but named something more related

    @wraps(route_func)
    def wrapper(*args, **kwargs):  # This can take ANY arguments
        # All logic goes inside here

        # 1) Check if the token exists
        raw_token = request.headers.get("Authorization")
        print(raw_token)

        # 2) if not token return Not Authorized
        if not raw_token:
            print("Token is not there.")
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

        # 3) Remove 'Bearer ' from the front
        token = raw_token.replace("Bearer ", "")
        print(token)

        try:
            # 4) This will decode a token, and will throw an exception if token is invalid
            payload = jwt.decode(token, SECRET, "HS256")
            print("payload done")

            # At this point you have a valid token

            # 5) get user from the token
            user_id = payload["sub"]
            print("UserID ", user_id)

            # 6) get user from this ID
            user = db.session.query(UserModel).get(user_id)

            # 7) Attach user to the request so we can use it later
            # Flask provides a globla obkject, g, that lets you attach info
            g.current_user = user
            print("Current User: ", g.current_user.username, g.current_user)

            # 8) Call my route
            return route_func(
                *args, **kwargs
            )  # need to return the callback with any arhuments added
        # When we decode the token, if tis expired, tell user its expired

        except jwt.ExpiredSignatureError:
            print("Expired")
            return {"message": "Token has expired"}, HTTPStatus.UNAUTHORIZED
        except Exception:
            print("Issue with token")
            return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED

    return wrapper
