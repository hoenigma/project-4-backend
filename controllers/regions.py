from http import HTTPStatus
from flask import Blueprint, request, jsonify, g
from marshmallow.exceptions import ValidationError
from app import db

# import info for the region and the secure route
from models.region import RegionModel
from models.area import AreaModel
from models.link import LinksModel
from models.threat import ThreatModel
from models.wildlife import WildlifeModel
from middleware.secure_route import secure_route
from serializers.region import RegionSchema

region_serializer = RegionSchema()

# import serializers for other tables
from serializers.area import AreaSchema
from serializers.link import LinkSchema
from serializers.threat import ThreatSchema
from serializers.wildlife import WildlifeSchema


router = Blueprint("regions", __name__)


# get all regions
@router.route("/regions", methods=["GET"])
def get_regions():
    try:
        regions = db.session.query(RegionModel).all()
        return region_serializer.jsonify(regions, many=True)
    except Exception as e:
        return jsonify({"message": "Failed to fetch regions", "error": str(e)}), 500


# get a region
@router.route("/region/<int:regionid>", methods=["GET"])
def get_single_region(regionid):
    try:
        region = db.session.query(RegionModel).get(regionid)
        return region_serializer.jsonify(region)

    except Exception as e:
        return jsonify({"message": "Failed to fetch the region", "error": str(e)}), 500


# update region
@router.route("/regions/<int:region_id>", methods=["PUT"])
@secure_route
def update_region(region_id):
    try:
        existing_region = db.session.query(RegionModel).get(region_id)
        print(existing_region)

        # get the role from the user
        current_userRole = g.current_user.roles
        print(current_userRole)

        # If the user has the role 2, they are an admin and can update:
        if current_userRole == 2:
            data = request.json
            region = region_serializer.load(
                data,
                instance=existing_region,  # This uses the existing game instead of
                partial=True,  # This will work if you dont provide all the data
            )

            # save region
            region.save()
            return region_serializer.jsonify(region)

        return {
            "message": "Unauthorized to update this region"
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


# Add a new region
@router.route("/regions", methods=["POST"])
@secure_route
def create_region():
    try:
        # get the role from the user
        current_userRole = g.current_user.roles
        print(current_userRole)

        # If the user has the role 2, they are an admin and can create:
        if current_userRole == 2:

            region_dictionary = request.json
            region_model = region_serializer.load(region_dictionary)
            region_model.save()

            return region_serializer.jsonify(region_model)

        return {"message": "Unauthorized to create a region"}, HTTPStatus.UNAUTHORIZED

    except ValidationError as e:
        return jsonify({"message": "something went wrong", "error": e.messages}), 422
    except Exception as e:
        print(e)
        return jsonify({"message": "something went wrong"}), 500


# delete region
@router.route("/regions/<int:region_id>", methods=["DELETE"])
@secure_route
def delete_region(region_id):
    try:
        # Check if there are any areas associated with the region
        areas = AreaModel.query.filter_by(region_id=region_id).all()

        if areas:
            # If there are associated areas, delete them first
            for area in areas:
                db.session.delete(area)
                db.session.commit()

        # Check if there are any links associated with the region
        links = LinksModel.query.filter_by(region_id=region_id).all()

        if links:
            # If there are associated links, delete them first
            for link in links:
                db.session.delete(link)
                db.session.commit()

        # Check if there are any threats associated with the region
        threats = ThreatModel.query.filter_by(region_id=region_id).all()

        if threats:
            # If there are associated threats, delete them first
            for threat in threats:
                db.session.delete(threat)
                db.session.commit()

        # Check if there are any wildlife associated with the region
        wildlives = WildlifeModel.query.filter_by(region_id=region_id).all()

        if wildlives:
            # If there are associated wildlives, delete them first
            for wildlife in wildlives:
                db.session.delete(wildlife)
                db.session.commit()

        region = db.session.query(RegionModel).get(region_id)
        if not region:
            return jsonify({"message": "Region not found"}), 404
        # get the role from the user
        current_userRole = g.current_user.roles
        print(current_userRole)

        # If the user has the role 2, they are an admin and can create:
        if current_userRole == 2:
            db.session.delete(region)
            db.session.commit()
            return region_serializer.jsonify(region)
        return {
            "message": "Unauthorized to delete this region"
        }, HTTPStatus.UNAUTHORIZED

    except Exception as e:
        # If an error occurs, rollback the session and return an error response
        db.session.rollback()
        return jsonify({"message": "Failed to delete region", "error": str(e)}), 500
