# from http import HTTPStatus
# from flask import Blueprint, request, jsonify
# from marshmallow.exceptions import ValidationError
# from app import db
# from models.user import UserModel
# from serializers.user import UserSerializer

# user_serializer = UserSerializer()

# router = Blueprint("users", __name__)


# @router.route("/signup", methods=["POST"])
# def signup():

#     try:
#         user_dictionary = request.json

#         user_model = user_serializer.load(user_dictionary)

#         db.session.add(user_model)
#         db.session.commit()

#         print("user model", user_model.password)

#         return user_serializer.jsonify(user_model)
#     except ValidationError as e:
#         return {
#             "errors": e.messages,
#             "message": "Something went wrong",
#         }, HTTPStatus.UNPROCESSABLE_ENTITY
#     except Exception as e:
#         print(e)
#         return {"message": "Something went wrong"}, HTTPStatus.INTERNAL_SERVER_ERROR
