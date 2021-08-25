from sqlalchemy.orm import relationship
from app import db


class Poi(db.Model):
    __tablename__ = 'poi'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    latitude = db.Column(db.Integer, nullable=False)
    longitude = db.Column(db.Integer, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('type.id'))

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "<User('%s','%s','%s')>" % \
               (self.name, self.latitude, self.longitude)


class Type(db.Model):
    __tablename__ = 'type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250), nullable=False)
    poi = relationship('Poi', backref='type', lazy='dynamic')

    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return "<User('%s')>" % self.type





