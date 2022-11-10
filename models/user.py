from init import db, ma
from marshmallow import fields

## User Model 
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    ##ForeignKeys
    ##project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    ## removed nullable = false constraint.

    projects = db.relationship('Project', back_populates='user', cascade='all, delete')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete')
   
    
# User Schema 
class UserSchema(ma.Schema):
    projects = fields.List(fields.Nested('ProjectSchema', exclude=['user']))
    comments = fields.List(fields.Nested('CommentSchema', exclude=['user']))
    
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'projects', 'comments')
        ordered = True


