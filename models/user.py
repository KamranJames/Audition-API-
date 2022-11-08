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
    projects = db.relationship('Project', back_populates='user', cascade='all, delete')
    projects = db.relationship('Comment', back_populates='user', cascade='all, delete')
    projects = db.relationship('Actor', back_populates='user', cascade='all, delete')
    projects = db.relationship('Casting', back_populates='user', cascade='all, delete')
    projects = db.relationship('Role', back_populates='user', cascade='all, delete')
# User Schema 
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')
        ordered = True


