from app import db
from sqlalchemy import String
from models.base import BaseModel


class WildlifeModel(db.Model, BaseModel):

    __tablename__ = "wildlife"

    region_id = db.Column(db.Integer, db.ForeignKey("regions.id"), nullable=False)

    id = db.Column(db.Integer, primary_key=True)

    wildlife = db.Column(db.ARRAY(String), nullable=False)

    # Relationship
    regions = db.relationship("RegionModel", back_populates="wildlife")
