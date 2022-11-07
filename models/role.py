from init import db, ma
from marshmallow import fields

#Role Model
class Role(db.Model):
     __tablename__ = 'roles'

     id = db.Column(db.Integer, primary_key=True)
     role = db.Column(db.String, nullable=False)
     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
     projects = db.relationship('Project', back_populates='roles', cascade='all, delete')
     
     

## Role Schema
class RoleSchema(ma.Schema):
    class Meta:
        fields = ('role', 'project') ##'actor'
        ordered = True

