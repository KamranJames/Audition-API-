from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

#Role Model
class Role(db.Model):
     __tablename__ = 'roles'

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(20), nullable=False)
     notes = db.Column(db.String(100), nullable=False)
     ##project = db.Column(db.String, nullable=False)

     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
     actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False)
    

     projects = db.relationship('Project', back_populates='roles')
     

## Role Schema
class RoleSchema(ma.Schema):
    project = fields.Nested('ProjectSchema')

    name = fields.String(required=True, validate=Length(min=1, max=20, error='Name must be at least 1 character min and 20 characters max'))
 
    
    class Meta:
        fields = ('id', 'name', 'project','notes', 'actor')
        ordered = True

