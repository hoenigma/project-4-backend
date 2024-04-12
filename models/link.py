from app import db
from models.base import BaseModel


class LinksModel(db.model, BaseModel):

    __tablename__ = "links"

    region_id = db.column(db.Integer, db.ForeignKey("regions.id"))
    links = db.Column(db.Text, nullable=False)

    # Relatiosnhip
    region = db.realtionship("RegionModel", back_populates="links")
