from app import db
from sqlalchemy import String
from models.base import BaseModel


class ThreatModel(db.Model, BaseModel):

    __tablename__ = "threats"

    region_id = db.Column(db.Integer, db.ForeignKey("regions.id"), nullable=False)
    id = db.Column(db.Integer, primary_key=True)

    threats = db.Column(db.ARRAY(String), nullable=False)

    # Relationship
    regions = db.relationship("RegionModel", back_populates="threats")
