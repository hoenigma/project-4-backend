from app import app, db
from models.user import UserModel
from models.region import RegionModel
from models.project import ProjectModel
from models.area import AreaModel
from models.threat import ThreatModel
from models.wildlife import WildlifeModel
from models.link import LinksModel
from models.base import BaseModel

with app.app_context():

    try:
        print("Creating our database...")
        db.drop_all()
        db.create_all()

        # seed regions
        region1 = RegionModel(
            country="England", region_name="South West", info="some info"
        )
        region1.save()

        # seed user
        user1 = UserModel(
            username="Matt123",
            email="matt@matt.com",
            name="Matt",
            roles=2,
            password="Password123!",
            # favourite_region=None,
        )
        user1.save()

        # seed project
        project1 = ProjectModel(
            user_id=user1.id,
            region_id=region1.id,
            # date="date",
            # time="time",
            name=user1.name,
            area_of_project="cornwall",
            description="ooohhh ocean",
            links="a long url",
        )
        project1.save()

        # seed Area
        area1 = AreaModel(
            region_id=region1.id,
            names=["Cornwall", "Devon", "Hampsted"],
            images=["image for cornwall", "image for devon", "image for hampsted"],
        )
        area1.save()

        # seed Threats
        threats1 = ThreatModel(
            region_id=region1.id, threats=["Costal Erosion", "pollution"]
        )
        threats1.save()

        # seed Wildlife
        wildlife1 = WildlifeModel(
            region_id=region1.id, wildlife=["seals, dolphins, crabs"]
        )
        wildlife1.save()

        # seed Links
        links1 = LinksModel(
            region_id=region1.id,
            links=["a url to this", "a url to that", "a url again!"],
        )
        links1.save()

        print("Database seeded!")

    except Exception as e:
        print(e)
