from marshmallow import fields
from app import marsh
from models.project import ProjectModel


class ProjectSchema(marsh.SQLAlchemyAutoSchema):

    users = fields.Nested("UserSerializer", many=False)

    class Meta:
        model = ProjectModel
        load_instance = True
