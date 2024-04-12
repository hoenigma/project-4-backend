from app import marsh
from models.link import LinksModel


class LinkSchema(marsh.SQLAlchemyAutoSchema):

    class Meta:
        model = LinksModel
        load_instance = True
