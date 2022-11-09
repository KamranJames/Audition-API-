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

     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
     
     roles = db.relationship("Role", back_populates="actors", cascade='all, delete')
     projects = db.relationship("Project", back_populates="actors", cascade='all, delete')
     
## Actor Schema
class ActorSchema(ma.Schema):
    role = fields.Nested('RoleSchema')
    project = fields.Nested('ProjectSchema')

    class Meta:
        fields = ('id','f_name', 'l_name', 'agency')
        ordered = True

