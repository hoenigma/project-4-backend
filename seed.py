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
        SW_england_region = RegionModel(
            country="England",
            region_name="South West England",
            image="https://www.aimovers.org.uk/uploads/news-pictures/3-new-york-blog-post-image-20210608133947.jpg",
            info="The South West if a diverse region of the english coast. Places like Cornwall and Devon are popular locations for surfers due to having an unitteupted cold dynamic Atlantic ocean coming ingto the penisula causing big swells. The Dorset coast also lives here which is a UNESCO World Heritage Site due to the amoutn of rare fossil reamins that have been found there. The South West also includes the Isle of Wight which has 13 beaches and the Isles of Scilly with picturesque, clear turquoise waters.",
        )
        SW_england_region.save()

        SE_england_region = RegionModel(
            country="England",
            region_name="South East England",
            image="https://www.map-of-uk.co.uk/maps/south-east-england.jpg",
            info=" The South East coast is over 300km long and is home to busy working ports including Dover, Folkestone and traditional seaside resorts like Eastbourne and Margate. The coast varies from the iconic White Cliffs of Dover to the shingle bay of the kent coast. It is also home to much history like Hastings and Herne Bay",
        )
        SE_england_region.save()

        NW_england_region = RegionModel(
            country="England",
            region_name="North West England",
            image="https://www.picturesofengland.com/images/mapofengland/north-west-map.gif",
            info="The Nort West hold a third of the population of the UK . This area includes Liverpool which was a key connection for England and Ireland and holds a mix of ports and sandy beaches in the Wirral. Further North we have the UK’s bussiest resort of Blackpool and The cumbria Coastal way, a footpath that is 182 miles long that goes to the Scottish Border.",
        )
        NW_england_region.save()

        NE_england_region = RegionModel(
            country="England",
            region_name="North East England",
            image="https://www.freeworldmaps.net/europe/united-kingdom/northeastengland/",
            info="Major port cities such as Grimsby, Hull and Newcastle are interspersed with rocky cliffs, windswept beaches, quaint fishing villages and bustling, family-friendly resort towns. Hull's maritime heritage dates back to Roman times and continues to evolve, with a fishing fleet, ferries, oil tankers and cargo ships docking regularly. A recently redeveloped marina and a stunning millenium building telling the story of the world's oceans, with the deepest acquarium tank in Europe, are both helping to put Hull on the tourist map. The three mile stretch of sand and shingle, known as Spurn Head, that leads to the mouth of the Humber estuary, is an important resting place for migratory birds. Hornsea and Withernsea are good shingle beaches north of Hull, with Withernsea stretching all the way to Bridlington, twenty miles further north. Just north of Bridlington is the spectacular Flamborough Head, a chalk headland that sticks out in proud contrast to the rugged shale cliffs either side.",
        )
        NE_england_region.save()

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
            region_id=SW_england_region.id,
            # date="date",
            # time="time",
            name=user1.name,
            area_of_project="cornwall",
            description="ooohhh ocean",
            links="a long url",
        )
        project1.save()

        project2 = ProjectModel(
            user_id=user1.id,
            region_id=SE_england_region.id,
            # date="date",
            # time="time",
            name=user1.name,
            area_of_project="dorset",
            description="ooohhh ocean",
            links="a long url",
        )

        project2.save()

        # seed Area
        SW_england_area = AreaModel(
            region_id=SW_england_region.id,
            names=[
                "Cornwall",
                "Devon",
                "Dorset",
                "Gloucestshire",
                "Hampshire",
                "Isle of Wight",
                "Isles of Scilly",
                "Somerset",
            ],
            images=[
                "https://www.sykescottages.co.uk/blog/wp-content/uploads/2021/02/Porthcurno-beach.jpg",
                "https://www.outandaboutlive.co.uk/images/image/Bantham_credit_Adobestock.jpg",
                "https://www.thebeachguide.co.uk/public/geophotos/50390144832sq.jpg",
                "https://cdn.soglos.com/images/outdoors/sg-outdoors-hotlist-bestbeaches-m5motorhomes-22.jpg?width=730&height=383&rmode=pad&bgcolor=ffffff&quality=85&format=webp",
                "https://www.visit-hampshire.co.uk/dbimgs/Hayling%20Island%20Beach%201%281%29.jpg",
                "https://www.sykescottages.co.uk/blog/wp-content/uploads/2021/11/Freshwater-Bay.jpg",
                "https://hips.hearstapps.com/hmg-prod/images/tresco-island-and-beyond-royalty-free-image-1591709910.jpg?crop=1.00xw:0.749xh;0,0.184xh&resize=1200:*",
                "https://a.cdn-hotels.com/gdcs/production58/d1100/dceededa-b941-479a-8d36-73dd3a278c57.jpg?impolicy=fcrop&w=1600&h=1066&q=medium",
            ],
        )
        SW_england_area.save()

        SE_england_area = AreaModel(
            region_id=SE_england_region.id,
            names=["East Sussex", "Essex", "Kent", "Norfolk", "Suffolk", "West Sussex"],
            images=[
                "https://www.thebeachguide.co.uk/south-east-england/east-sussex/birling-gap.htm",
                "https://www.thebeachguide.co.uk/public/geophotos/50390144804.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/24680232222.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/49001791052.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/29112036785.jpg",
            ],
        )
        SE_england_area.save()

        NW_england_area = AreaModel(
            region_id=NW_england_region.id,
            names=["Cumbria", "Lancashire", "Merseyside"],
            images=[
                "https://www.thebeachguide.co.uk/public/geophotos/43981372815.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/2983076.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/3557719.jpg",
            ],
        )
        NW_england_area.save()

        NE_england_area = AreaModel(
            region_id=NE_england_region.id,
            names=[
                "County Durham",
                "Lincolnshire",
                "Northumberland",
                "Tyne and Wear",
                "Yorkshire",
            ],
            images=[
                "https://www.thebeachguide.co.uk/public/geophotos/1582649.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/1850153.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/3797370.jpg",
                "https://www.thebeachguide.co.uk/public/geophotos/521882.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/3242444472.jpg",
            ],
        )
        NE_england_area.save()

        # seed Threats
        SW_england_threats = ThreatModel(
            region_id=SW_england_region.id,
            threats=[
                "Ocean Acidification",
                "Rainfall",
                "wave height increase",
                "leads to costal errosion and cliffs falling",
            ],
        )
        SW_england_threats.save()

        SE_england_threats = ThreatModel(
            region_id=SE_england_region.id,
            threats=[
                "Ocean Acidification (esepcially for chalk cliffs)",
                "Rainfall",
                "Drying out of wetlands",
                "loss of tourist economy (2nd biggest in England)",
            ],
        )
        SE_england_threats.save()

        NW_england_threats = ThreatModel(
            region_id=NW_england_region.id,
            threats=["Flooding", "Climate Change", "Pollution"],
        )
        NW_england_threats.save()

        NE_england_threats = ThreatModel(
            region_id=NE_england_region.id,
            threats=[
                "Coastal erosion (loss of Alnmouth Village golf club)",
                "Pollution from old landfill site",
                "trawlling",
                "noise pollution",
            ],
        )
        NE_england_threats.save()

        # seed Wildlife
        SW_england_wildlife = WildlifeModel(
            region_id=SW_england_region.id,
            wildlife=[
                "Grey Seals",
                "Beavers",
                "Common Dolphin",
                "sand dunes",
                "moorland",
                "coastal cliffs",
                "saltwater marshs",
            ],
        )
        SW_england_wildlife.save()

        SE_england_wildlife = WildlifeModel(
            region_id=SE_england_region.id,
            wildlife=[
                "Common Crab",
                "Puffin",
                "Bottlenose Dolphin",
                "sand dunes",
                "moorland",
                "coastal cliffs",
                "saltwater marshs",
                "sand dunes",
            ],
        )
        SE_england_wildlife.save()

        NW_england_wildlife = WildlifeModel(
            region_id=NW_england_region.id,
            wildlife=["Eastiarues", "Basking Sharks", "Atlantic Bluefin Tuna"],
        )
        NW_england_wildlife.save()

        NE_england_wildlife = WildlifeModel(
            region_id=NE_england_region.id,
            wildlife=[
                "Wild Oysters",
                "Minke Whales",
                "Eiders",
                "sandy shores",
                "salt marshes",
            ],
        )
        NE_england_wildlife.save()

        # seed Links
        SW_england_links = LinksModel(
            region_id=SW_england_region.id,
            links=[
                "https://www.southwestcoastpath.org.uk/",
                "https://www.cornwallwildlifetrust.org.uk/what-we-do/our-conservation-work/at-sea/seaquest-southwest",
                "https://www.nationaltrust.org.uk/visit/dorset/studland-bay/coastal-erosion-at-studland-bay",
            ],
        )
        SW_england_links.save()

        SE_england_links = LinksModel(
            region_id=SE_england_region.id,
            links=[
                "https://se-coastalgroup.org.uk/our-coastline/",
                "https://www.ukcip.org.uk/wp-content/PDFs/SE_summary.pdf",
                "https://www.kentwildlifetrust.org.uk/our-work/our-projects",
            ],
        )
        SE_england_links.save()

        NW_england_links = LinksModel(
            region_id=NW_england_region.id,
            links=[
                "https://www.geospatialuk.org/post/protecting-the-coastlines-of-the-north-west-british-isles",
                "https://www.mycoastline.org.uk/",
                "https://www.kentwildlifetrust.org.uk/our-work/our-projects",
                "https://www.livingseasnw.org.uk/what-we-do/marine-conservation-projects",
            ],
        )
        NW_england_links.save()

        NE_england_links = LinksModel(
            region_id=NE_england_region.id,
            links=[
                "https://www.nhsn.org.uk/citizen-science-marine/",
                "https://www.durhamwt.com/projects",
                "https://www.nationaltrust.org.uk/visit/north-east/souter-lighthouse-and-the-leas/whitburn-coastal-conservation-centre-project",
            ],
        )

        NE_england_links.save()

        print("Database seeded!")

    except Exception as e:
        print(e)
