from app import db
from models.area import AreaModel
from models.wildlife import WildlifeModel
from models.threat import ThreatModel
from models.link import LinksModel
from models.base import BaseModel


class RegionModel(db.Model, BaseModel):

    __tablename__ = "regions"

    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.Text, nullable=False)
    region_name = db.Column(db.Text, nullable=False)
    info = db.Column(db.Text, nullable=False)

    # Relationships
    areas = db.relationship("AreaModel", back_populates="regions")
    links = db.relationship("LinksModel", back_populates="regions")
    threats = db.relationship("ThreatModel", back_populates="regions")
    wildlife = db.relationship("WildlifeModel", back_populates="regions")
    projects = db.relationship("ProjectModel", back_populates="regions")
    users = db.relationship("UserModel", back_populates="regions")
