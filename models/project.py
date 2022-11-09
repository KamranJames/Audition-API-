from init import db, ma
from marshmallow import fields

#Project Model
class Project(db.Model):
     __tablename__ = 'projects'

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String, nullable=False)
     director = db.Column(db.String, nullable=False)
     year = db.Column(db.String, nullable=False)
    
     
     
     
     ##ForeignKeys
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
     ##role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
     ##project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
   

     
     user = db.relationship('User', back_populates ='projects', cascade='all, delete')
     castings = db.relationship('Casting', back_populates ='projects', cascade='all, delete')
     actors = db.relationship('Actor', back_populates ='projects', cascade='all, delete')
     comments = db.relationship('Comment', back_populates ='projects', cascade='all, delete')
     roles = db.relationship('Role', back_populates ='projects', cascade='all, delete')

## Project Schema
class ProjectSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    comments = fields.List(fields.Nested('CommentSchema', exclude=['project']))

    class Meta:
        fields = ('id','name', 'director', 'year', 'comments', 'user')
        ordered = True


