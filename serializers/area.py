from app import marsh
from models.area import AreaModel


class AreaSchema(marsh.SQLAlchemyAutoSchema):

    class Meta:
        model = AreaModel
        load_instance = True
