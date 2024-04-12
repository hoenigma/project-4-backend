from app import db
from sqlalchemy import String
from models.base import BaseModel


class LinksModel(db.Model, BaseModel):

    __tablename__ = "links"

    region_id = db.Column(db.Integer, db.ForeignKey("regions.id"), nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    links = db.Column(db.ARRAY(String), nullable=False)

    # Relatiosnhip
    regions = db.relationship("RegionModel", back_populates="links")
