from app import app,db
from models.user import UserModel
from models.region import RegionModel
from models.area import AreaModel
from models.threat import ThreatsModel
from models.wildlife import WildlifeModel
from models.link import LinksModel
from models.base import BaseModel

with app.app_context():

    try:
        print("Creating our database...")
        db.drop_all()
        db.create_all()

        # seed user
        user = UserModel(username="Matt123", email="matt@matt.com", name="Matt", roles=2, password="Password123!" )
        user.save()

        # seed regions
        

        