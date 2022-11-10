from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length


## User Model 
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    


    projects = db.relationship('Project', back_populates='user', cascade='all, delete')
    comments = db.relationship('Comment', back_populates='user', cascade='all, delete')
   
    
# User Schema 
class UserSchema(ma.Schema):
    projects = fields.List(fields.Nested('ProjectSchema', exclude=['user']))
    comments = fields.List(fields.Nested('CommentSchema', exclude=['user']))

    name = fields.String(required=True, validate=Length(min=1, max=20, error='Name must be at least 1 character min and 20 characters max'))

    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'projects', 'comments')
        ordered = True


