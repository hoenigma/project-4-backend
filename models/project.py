from app import db
from models.user import UserModel
from models.region import RegionModel
from models.base import BaseModel


class ProjectModel(db.Model, BaseModel):

    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey("regions.id"), nullable=False)

    # Date and time will be automatic
    date = db.Column(db.Text, nullable=False)
    time = db.Column(db.Text, nullable=False)

    # They will type this in
    name = db.Column(db.Text, nullable=False)
    area_of_project = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    links = db.Column(db.Text, nullable=True)

    # Adding other modles to projects
    users = db.relationship("UserModel", back_populates="projects")
    regions = db.relationship("RegionModel", back_populates="projects")
