from http import HTTPStatus
from flask import Blueprint, request, jsonify, g
from marshmallow.exceptions import ValidationError
from app import db
from models.project import ProjectModel
from middleware.secure_route import secure_route
from serializers.project import ProjectSchema

project_serializer = ProjectSchema()

router = Blueprint("projects", __name__)


# Get all projects for one REGION
@router.route("/projects/<int:region_id>", methods=["GET"])
def get_projects_by_region(region_id):
    try:
        # use filter_by to get the projects that have the same region_id
        projects = db.session.query(ProjectModel).filter_by(region_id=region_id).all()
        return project_serializer.jsonify(projects, many=True)
    except Exception as e:
        return jsonify({"message": "Failed to fetch projects", "error": str(e)}), 500


# Get one project
@router.route("/project/<int:project_id>", methods=["GET"])
def get_one_project(project_id):
    try:
        project = db.session.query(ProjectModel).get(project_id)
        return project_serializer.jsonify(project)

    except Exception as e:
        return jsonify({"message": "Failed to fetch the region", "error": str(e)}), 500


# Get all projects for one USER (show in user page)
@router.route("/user/projects", methods=["GET"])
@secure_route
def get_projects_by_user():
    try:
        current_userId = g.current_user.id
        print("The current userID is ", current_userId)
        # use filter_by to get the projects that have the same region_id
        projects = (
            db.session.query(ProjectModel).filter_by(user_id=current_userId).all()
        )
        return project_serializer.jsonify(projects, many=True)
    except Exception as e:
        return jsonify({"message": "Failed to fetch projects", "error": str(e)}), 500


# update a project
@router.route("/updateprojects/<int:project_id>", methods=["PUT"])
@secure_route
def update_project(project_id):
    try:
        # get the id from the user
        current_userId = g.current_user.id
        print("The current userID is ", current_userId)

        existing_project = db.session.query(ProjectModel).get(project_id)
        print("The existing project", existing_project)

        userId_from_project = existing_project.user_id
        print("The project userID is ", userId_from_project)

        if current_userId == userId_from_project:
            data = request.json
            project = project_serializer.load(
                data,
                instance=existing_project,
                partial=True,
            )

            # save project
            project.save()
            return project_serializer.jsonify(project)
        return {
            "message": "Unauthorized to update this project"
        }, HTTPStatus.UNAUTHORIZED

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


# Create a project
@router.route("/projects/add/<int:region_id>", methods=["POST"])
@secure_route
def add_project(region_id):
    try:
        # get the id from the user
        current_userId = g.current_user.id
        print("The current userID is ", current_userId)
        project_dictionary = request.json
        # give the project the userId
        project_dictionary["user_id"] = current_userId
        # give the project the region its for
        project_dictionary["region_id"] = region_id

        print(project_dictionary)

        project_model = project_serializer.load(project_dictionary)

        project_model.save()

        return project_serializer.jsonify(project_model)

    except ValidationError as e:
        return jsonify({"message": "something went wrong", "error": e.messages}), 422
    except Exception as e:
        print(e)
        return jsonify({"message": "something went wrong"}), 500


# Delete a project
@router.route("/projects/<int:project_id>", methods=["DELETE"])
@secure_route
def delete_project(project_id):
    try:
        # get the id from the user
        current_userId = g.current_user.id
        print("The current userID is ", current_userId)

        project = db.session.query(ProjectModel).get(project_id)
        print(project)

        userId_from_project = project.user_id
        print("The project userID is ", userId_from_project)

        if current_userId == userId_from_project:

            db.session.delete(project)
            db.session.commit()
            return project_serializer.jsonify(project)
        return {
            "message": "Unauthorized to delete this project"
        }, HTTPStatus.UNAUTHORIZED

    except Exception as e:
        # If an error occurs, rollback the session and return an error response
        db.session.rollback()
        return jsonify({"message": "Failed to delete project", "error": str(e)}), 500
