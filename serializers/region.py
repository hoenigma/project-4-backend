from marshmallow import fields
from app import marsh
from models.region import RegionModel


class RegionSchema(marsh.SQLAlchemyAutoSchema):

    areas = fields.Nested("AreaSchema", many=True)
    links = fields.Nested("LinkSchema", many=True)
    threats = fields.Nested("ThreatSchema", many=True)
    wildlife = fields.Nested("WildlifeSchema", many=True)

    class Meta:
        model = RegionModel
        load_instance = True
