from marshmallow import fields
from app import marsh
from models.project import ProjectModel


class ProjectSchema(marsh.SQLAlchemyAutoSchema):

    users = fields.Nested("UserSerializer", many=False)
    # Define region_id and user_id fields
    region_id = fields.Integer(required=True)
    user_id = fields.Integer(required=True)

    class Meta:
        model = ProjectModel
        load_instance = True
