from app import marsh
from models.project import ProjectModel


class ProjectSchema(marsh.SQLAlchemyAutoSchema):

    class Meta:
        model = ProjectModel
        load_instance = True
