from app import marsh
from models.wildlife import WildlifeModel


class WildlifeSchema(marsh.SQLAlchemyAutoSchema):

    class Meta:
        model = WildlifeModel
        load_instance = True
