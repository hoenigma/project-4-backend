from app import db
from models.base import BaseModel


class WildlifeModel(db.model, BaseModel):

    __tablename__ = "wildlife"

    region_id = db.column(db.Integer, db.ForeignKey("regions.id"))
    wildlife = db.Column(db.Text, nullable=False)

    # Relationship
    region = db.realtionship("RegionModel", back_populates="wildlife")
