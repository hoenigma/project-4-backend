from app import db
from models.base import BaseModel


class ThreatModel(db.model, BaseModel):

    __tablename__ = "threats"

    region_id = db.column(db.Integer, db.ForeignKey("regions.id"))
    threats = db.Column(db.Text, nullable=False)

    # Relationship
    region = db.realtionship("RegionModel", back_populates="threats")
