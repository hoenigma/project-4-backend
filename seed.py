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
            image="https://www.researchgate.net/profile/Audley-Genus-2/publication/254346577/figure/fig1/AS:297951793565698@1448048651825/Map-of-North-East-England-Source-One-North-East.png",
            info="Major port cities such as Grimsby, Hull and Newcastle are interspersed with rocky cliffs, windswept beaches, quaint fishing villages and bustling, family-friendly resort towns. Hull's maritime heritage dates back to Roman times and continues to evolve, with a fishing fleet, ferries, oil tankers and cargo ships docking regularly. A recently redeveloped marina and a stunning millenium building telling the story of the world's oceans, with the deepest acquarium tank in Europe, are both helping to put Hull on the tourist map. The three mile stretch of sand and shingle, known as Spurn Head, that leads to the mouth of the Humber estuary, is an important resting place for migratory birds. Hornsea and Withernsea are good shingle beaches north of Hull, with Withernsea stretching all the way to Bridlington, twenty miles further north. Just north of Bridlington is the spectacular Flamborough Head, a chalk headland that sticks out in proud contrast to the rugged shale cliffs either side.",
        )
        NE_england_region.save()

        northern_ireland_region = RegionModel(
            country="Ireland",
            region_name="Northern Ireland",
            image="https://cdn.pixabay.com/photo/2012/04/11/15/48/ireland-28617_1280.png",
            info="The Northern Ireland coastline is one of Britain's hidden gems, with over two hundred diverse kilometers in the care of the National Trust. The Causeway Coast holds the Giant's Causeway which is Northern Irelands's only World Herritage Site. County Londonderry contains the popular seaside resort of Portstewart, close to the excellent Portstewart Strand, a two mile stretch of golden sand, backed by dunes. Another excellent beach can be found near the tranquil resort of Castlerock. The dunes here are among the oldest in Ireland and extend upstream to a National Trust bird sanctuary.",
        )
        northern_ireland_region.save()

        ireland_region = RegionModel(
            country="Ireland",
            region_name="Republic Of Ireland",
            image="https://gisgeography.com/wp-content/uploads/2017/10/Ireland-Map-678x805.jpg",
            info="Ireland's three-thousand-kilometer coastline is a place of stunning variety. The wild west, with its massive cliffs and huge waves sits in contrast to the more sheltered east, with its energetic and cosmopolitan cities, pretty villages and sheltered bays. Cork is the biggest county in Ireland, boasting a rugged west coast, attractive towns such as Clonakilty and popular surfing beaches such as Inchydory, located on an island connected to the mainland by two causeways.The peninsulas of Kerry are renowned for their excellent spas, while Clare is home to one of Ireland's top tourist attractions, the towering Cliffs of Moher, which belong to the UNESCO-supported Global Geopark Network and attract close to a million visitors every year.",
        )
        ireland_region.save()

        north_scotland_region = RegionModel(
            country="Scotland",
            region_name="North Scotland",
            image="https://i0.wp.com/www.awaywithmaja.com/wp-content/uploads/2020/10/Screen-Shot-2020-10-05-at-10.21.35-AM.png?w=705&ssl=1",
            info="Sparsely populated, with an often hostile climate, the coastline of Northern Scotland consists of a large area of unspoilt scenery clinging on to the edge of Europe. Heading north from the Moray Firth, on the east coast, the low-lying landscape becomes increasingly dramatic, with spectacular cliffs, swirling seas and rugged offshore islands. John O'Groats is billed as the most northerly point on the British Isles, although the wilder and less commercial Dunnet Head contests this title. Dunnet Head lies between Thurso and Wick, the main settlements on the north shore. Both towns are folded around small harbours and still depend largely on fishing for their survival, although tourism plays an increasingly important role. Every surfer will have heard tales of Thurso East, a heavy reefbreak that is firmly on the world surfing map, despite the frequently freezing conditions.",
        )
        north_scotland_region.save()

        south_scotland_region = RegionModel(
            country="Scotland",
            region_name="South Scotland",
            image="https://dwn-cdn.dash4it.co.uk/media/catalog/product/cache/7e486ee801cc6620aea65ca981d4bcc2/s/o/south-scotland-postcode-district-wall-map-d5.jpg",
            info="South Scotland is more populated and accessible than the wild north, although much of its coastline remains beautifully unspoilt. The area north of Edinburgh, Scotland's capital, is easily explored via the Fife Coastal Path, which meets the Southern Upland Way at Pease Bay, a sweeping sandy beach and well-known surfing destination. St Andrew's is home to the third oldest university in the English-speaking world and a world-famous golf course. Captain Scott's RRS Discovery is permanently moored in the historic port town of Dundee, which sits on the banks of the River Tay, while Broughty Ferry, a Victorian seaside resort, offers excellent views over the Tay estuary.",
        )
        south_scotland_region.save()

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
            name_of_project="Beach Clean up at Porthcurno",
            area_of_project="cornwall",
            date_time="Saturday 27th April, 2pm",
            description="ooohhh ocean",
            links="a long url",
        )
        project1.save()

        project2 = ProjectModel(
            user_id=user1.id,
            region_id=SE_england_region.id,
            # date="date",
            # time="time",
            name_of_project="Sand dunes talk at Studland",
            area_of_project="dorset",
            date_time="Thursday 9th May, 11am",
            description="ooohhh sand",
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
                "https://www.thebeachguide.co.uk/public/geophotos/19412775314.jpg",
                "https://www.thebeachguide.co.uk/public/geophotos/50390144804.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/24680232222.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/49001791052.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/1255934.webp",
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

        northern_ireland_area = AreaModel(
            region_id=northern_ireland_region.id,
            names=["County Antrim", "County Down", "Country Londonderry"],
            images=[
                "https://www.thebeachguide.co.uk/public/geophotos/785899.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/3276060.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/52714105575.webp",
            ],
        )
        northern_ireland_area.save()

        ireland_area = AreaModel(
            region_id=ireland_region.id,
            names=[
                "County Clare",
                "County Cork",
                "Country Donegal",
                "County Dublin",
                "County Galway",
                "County Kerry",
                "County Louth",
                "County Mayo",
                "County Sligo",
                "County Waterford",
                "County Wexford",
                "County Wicklow",
            ],
            images=[
                "https://www.thebeachguide.co.uk/public/geophotos/4946851.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/52696847449.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/1919633.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/52696847485.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/1366326.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/52672810596.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/52714105604.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/52696847447.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/52696847488.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/835535.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/5017477.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/52714105573.webp",
            ],
        )
        ireland_area.save()

        north_scotland_area = AreaModel(
            region_id=north_scotland_region.id,
            names=[
                "Grampain",
                "Hebrides",
                "Highland",
                "Orkney Islands",
                "Shetland Islands",
            ],
            images=[
                "https://www.thebeachguide.co.uk/public/geophotos/684750.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/52714105624.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/665342.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/3112646.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/1307216.webp",
            ],
        )
        north_scotland_area.save()

        south_scotland_area = AreaModel(
            region_id=south_scotland_region.id,
            names=[
                "Dumfries and Galloway",
                "Fife",
                "Lothian",
                "Scottish Borders",
                "Strathclyde",
                "Tayside",
            ],
            images=[
                "https://www.thebeachguide.co.uk/public/geophotos/2733914.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/4718900.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/30080375147.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/138169.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/3353343.webp",
                "https://www.thebeachguide.co.uk/public/geophotos/2112462615.jpg",
            ],
        )
        south_scotland_area.save()

        # seed Threats
        SW_england_threats = ThreatModel(
            region_id=SW_england_region.id,
            threats=[
                "Ocean Acidification",
                "Rainfall",
                "Wave Height Increase",
                "Costal errosion and cliffs falling",
            ],
        )
        SW_england_threats.save()

        SE_england_threats = ThreatModel(
            region_id=SE_england_region.id,
            threats=[
                "Ocean Acidification (esepcially for the chalk cliffs)",
                "Rainfall",
                "Drying out of Wetlands",
                "Loss of Tourist Economy (2nd biggest in England)",
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
                "Coastal Erosion (loss of Alnmouth Village golf club)",
                "Pollution from Old Landfill Site",
                "Trawlling",
                "Noise Pollution",
            ],
        )
        NE_england_threats.save()

        northern_ireland_threats = ThreatModel(
            region_id=northern_ireland_region.id,
            threats=[
                "Habitat lost from agriculture and urbanisation",
                "Invasive species",
                "Cliamte Change",
            ],
        )
        northern_ireland_threats.save()

        ireland_threats = ThreatModel(
            region_id=ireland_region.id,
            threats=["Coatal Erosion", "Overfishing", "Habitat Destruction"],
        )
        ireland_threats.save()

        north_scotland_threats = ThreatModel(
            region_id=north_scotland_region.id,
            threats=[
                "Habitat Fragmnetation",
                "Illegal Poaching",
                "Climate Changebaffecting ecosystems link Peat Bogs",
            ],
        )
        north_scotland_threats.save()

        south_scotland_threats = ThreatModel(
            region_id=south_scotland_region.id,
            threats=[
                "Habitat Fragmnetation",
                "Illegal Poaching",
                "Climate Changebaffecting ecosystems link Peat Bogs",
            ],
        )
        south_scotland_threats.save()

        # seed Wildlife
        SW_england_wildlife = WildlifeModel(
            region_id=SW_england_region.id,
            wildlife=[
                "Grey Seals",
                "Beavers",
                "Common Dolphin",
                "Sand Dunes",
                "Moorland",
                "Coastal Cliffs",
                "Saltwater Marshes",
            ],
        )
        SW_england_wildlife.save()

        SE_england_wildlife = WildlifeModel(
            region_id=SE_england_region.id,
            wildlife=[
                "Common Crab",
                "Puffin",
                "Bottlenose Dolphin",
                "Sand dunes",
                "Moorland",
                "Coastal Cliffs",
                "Saltwater Marshes",
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
                "Sandy Shores",
                "Salt Marshes",
            ],
        )
        NE_england_wildlife.save()

        northern_ireland_wildlife = WildlifeModel(
            region_id=northern_ireland_region.id,
            wildlife=[
                "Irish Stoats",
                "Puffins",
                "Razorbills",
                "Thornback Ray",
                "Orcas",
            ],
        )
        northern_ireland_wildlife.save()

        ireland_wildlife = WildlifeModel(
            region_id=ireland_region.id,
            wildlife=[
                "Irish Stoats",
                "Puffins",
                "Gray Seals",
                "Salmon",
                "Kelp Forests",
            ],
        )
        ireland_wildlife.save()

        north_scotland_wildlife = WildlifeModel(
            region_id=north_scotland_region.id,
            wildlife=["Red Squirrels", "Golden Eagles", "Ospreys", "Otters", "Seals"],
        )
        north_scotland_wildlife.save()

        south_scotland_wildlife = WildlifeModel(
            region_id=south_scotland_region.id,
            wildlife=["Red Squirrels", "Golden Eagles", "Ospreys", "Otters", "Seals"],
        )
        south_scotland_wildlife.save()

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

        northern_ireland_links = LinksModel(
            region_id=northern_ireland_region.id,
            links=[
                "https://www.ulsterwildlife.org/",
                "https://www.rspb.org.uk/northern-ireland",
                "https://www.ulsterwildlife.org/nature-recovery-networks",
            ],
        )

        northern_ireland_links.save()

        ireland_links = LinksModel(
            region_id=ireland_region.id,
            links=[
                "https://www.npws.ie/",
                "https://cleancoasts.org/",
                "https://www.coastwatch.org/",
            ],
        )
        northern_ireland_links.save()

        north_scotland_links = LinksModel(
            region_id=north_scotland_region.id,
            links=[
                "https://scottishwildlifetrust.org.uk/",
                "https://www.mcsuk.org/",
                "https://www.seabird.org/",
            ],
        )
        north_scotland_links.save()

        south_scotland_links = LinksModel(
            region_id=south_scotland_region.id,
            links=[
                "https://www.coastalcommunities.co.uk/",
                "https://scottishwildlifetrust.org.uk/",
                "https://hwdt.org/",
            ],
        )
        south_scotland_links.save()

        print("Database seeded!")

    except Exception as e:
        print(e)
