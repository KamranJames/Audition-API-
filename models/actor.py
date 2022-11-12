from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length


## Model 
#Actor Model
class Actor(db.Model):
     __tablename__ = 'actors'

     id = db.Column(db.Integer, primary_key=True)
     f_name = db.Column(db.String(20), nullable=False)
     l_name = db.Column(db.String(20), nullable=False)
     agency = db.Column(db.String(20), nullable=False)

## Foreign Key
     project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
     
     projects = db.relationship("Project", back_populates="actors", cascade='all, delete' )
     
## Actor Schema
class ActorSchema(ma.Schema):
    role = fields.Nested('RoleSchema')
    project = fields.Nested('ProjectSchema')
 
    f_name = fields.String(required=True, validate=Length(min=1, max=20, error='First name must be at least 1 character min and 20 characters max'))
    l_name = fields.String(required=True, validate=Length(min=1, max=20, error='Last Name must be at least 1 character min and 20 characters max'))

   

    class Meta:
        fields = ('id','f_name', 'l_name', 'agency', 'project_id', 'roles')
        ordered = True

