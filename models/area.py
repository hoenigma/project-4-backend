from app import db
from models.base import BaseModel


class AreaModel(db.model, BaseModel):

    __tablename__ = "areas"

    region_id = db.column(db.Integer, db.ForeignKey("regions.id"))

    names = db.Column(db.Text, nullable=False)
    images = db.Column(db.Text, nullable=False)

    # Relationship
    region = db.realtionship("RegionModel", back_populates="areas")
