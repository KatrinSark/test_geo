from app import db
from models import Poi, Type


# type = 'музей'
# name = 'Русский музей'
# latitude = 59.939509784516105
# longitude = 30.318372528133985
#
# newPoi = Poi(name, latitude, longitude)
# newType = Type(type)
# db.session.add(newType)
# db.session.add(newPoi)
# newType.poi.append(newPoi)
#
#
# db.session.commit()
# db.session.close()

name = 'музей'
poi_list = []
pois = Poi.query.filter(Poi.name.contains(name)).all()
if len(pois) == 0:
    data = {
        'data': 'Такого места нет в базе.'
    }
else:
    for poi in pois:
        poi_list.append(poi.name)
    data = {
        'data': poi_list
    }

print(data)
