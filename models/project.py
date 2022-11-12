from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length, OneOf

#Valid inputs for status field in Project.
VALID_STATUSES = ('Filming', 'Pre-Production', 'Post-Production', 'Development')

#Project Model
class Project(db.Model):
     __tablename__ = 'projects'

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String(20), nullable=False)
     director = db.Column(db.String(30), nullable=False)
     year = db.Column(db.String(30), nullable=False)
     status = db.Column(db.String(30), default=VALID_STATUSES[0])
    
     
     
     
     ##ForeignKeys
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
 
     user = db.relationship('User', back_populates ='projects', cascade='all, delete')
     castings = db.relationship('Casting', back_populates ='projects', cascade='all, delete')
     actors = db.relationship('Actor', back_populates ='projects', cascade='all, delete')
     comments = db.relationship('Comment', back_populates ='projects', cascade='all, delete')
     roles = db.relationship('Role', back_populates ='projects',)

## Project Schema
class ProjectSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    comments = fields.List(fields.Nested('CommentSchema', exclude=['project']))
    name = fields.String(required=True, validate=Length(min=1, max=20, error='Name must be at least 1 character min and 20 characters max'))
    status = fields.String(required=True, validate=OneOf(VALID_STATUSES))

    class Meta:
        fields = ('id','name', 'director', 'year', 'status', 'comments', 'user_id', 'casting_id', 'actor_id', 'role_id')
        ordered = True


