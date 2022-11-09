from init import db, ma
from marshmallow import fields

#Role Model
class Role(db.Model):
     __tablename__ = 'roles'

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String, nullable=False)
     ##project = db.Column(db.String, nullable=False)

     ##project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    

     projects = db.relationship('Project', back_populates='roles', cascade='all, delete')
     actors = db.relationship('Actor', back_populates='roles', cascade='all, delete')
     

## Role Schema
class RoleSchema(ma.Schema):
    class Meta:
        projects = fields.Nested('ProjectSchema', only=['name'])
        fields = ('id', 'name', 'project')
        ordered = True

