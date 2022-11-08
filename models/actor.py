from init import db, ma
from marshmallow import fields

## Model 
#Actor Model
class Actor(db.Model):
     __tablename__ = 'actors'

     id = db.Column(db.Integer, primary_key=True)
     f_name = db.Column(db.String, nullable=False)
     l_name = db.Column(db.String, nullable=False)
     agency = db.Column(db.String, nullable=False)
     ## Learn how to add FK here audition_id

## Actor Schema
class ActorSchema(ma.Schema):
    class Meta:
        fields = ('f_name', 'l_name', 'agency')
        ordered = True