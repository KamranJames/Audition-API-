from init import db, ma
from marshmallow import fields


## Casting Model
class Casting(db.Model):
     __tablename__ = 'castings'

     id = db.Column(db.Integer, primary_key=True)
     ## cd is short for casting director
     cd = db.Column(db.String, nullable=False)
     location = db.Column(db.String, nullable=False)
     
     #Foreign Keys
     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
     projects = db.relationship("Project", back_populates="castings", cascade='all, delete')

## Casting Schema
class CastingSchema(ma.Schema):
    class Meta:
       ##cd is short for casting director
       fields = ('id','cd', 'location')
       ordered = True