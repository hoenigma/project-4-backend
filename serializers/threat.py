from app import marsh
from models.threat import ThreatModel


class ThreatSchema(marsh.SQLAlchemyAutoSchema):

    class Meta:
        model = ThreatModel
        load_instance = True
