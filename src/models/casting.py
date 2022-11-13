from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length


## Casting Model
class Casting(db.Model):
     __tablename__ = 'castings'

     id = db.Column(db.Integer, primary_key=True)
     casting_assosciate = db.Column(db.String(20), nullable=False)
     location = db.Column(db.String(30), nullable=False)
     agency = db.Column(db.String(30), nullable=False)
     
     #Foreign Keys
     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
     
     projects = db.relationship("Project", back_populates="castings")

## Casting Schema
class CastingSchema(ma.Schema):
    projects = fields.Nested('ProjectSchema')

    casting_assosciate = fields.String(required=True, validate=Length(min=1, max=20, error='Assosciate must be at least 1 character min and 20 characters max'))


    class Meta:
       fields = ('id','casting_assosciate', 'agency', 'location', 'project_id')
       ordered = True