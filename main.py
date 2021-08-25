from app import app, db
from flask import request, jsonify
from models import Poi, Type

db.create_all()

@app.route('/get_by_type', methods=['GET'])
def get_by_type():
    type_name = request.args.get('type')
    poi_list = []
    type = Type.query.filter_by(type=type_name).first()
    if type == None:
        data = {
            'data': 'Такой категории в базе нет',
        }
        return jsonify(data)
    else:
        for poi in type.poi:
            poi_list.append(poi)
        data = {
            'data': poi_list
        }
    return jsonify(data)


@app.route('/get_by_name', methods=['GET'])
def get_by_name():
    name = request.args.get('name')
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
    return jsonify(data)

if __name__ == '__main__':
    app.run()
