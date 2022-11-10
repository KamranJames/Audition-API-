from init import db, ma
from marshmallow import fields

#Role Model
class Role(db.Model):
     __tablename__ = 'roles'

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String, nullable=False)
     ##project = db.Column(db.String, nullable=False)

     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    

     ##projects = db.relationship('Project', back_populates='roles')
     actors = db.relationship('Actor', back_populates='roles')
     

## Role Schema
class RoleSchema(ma.Schema):
    actors = fields.Nested('ActorSchema')
    
    class Meta:
        fields = ('id', 'name', 'project', 'actors')
        ordered = True

