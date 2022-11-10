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

## Foreign Key
     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
     
     projects = db.relationship("Project", back_populates="actors")
     
## Actor Schema
class ActorSchema(ma.Schema):
    role = fields.Nested('RoleSchema')
    project = fields.Nested('ProjectSchema')

    class Meta:
        fields = ('id','f_name', 'l_name', 'agency', 'project_id', 'roles')
        ordered = True

