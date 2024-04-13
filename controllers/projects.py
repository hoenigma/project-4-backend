from flask import Blueprint, request, jsonify, g
from app import db
from models.project import ProjectModel
from middleware.secure_route import secure_route
from serializers.project import ProjectSchema

router = Blueprint("projects", __name__)

# Get all posts
