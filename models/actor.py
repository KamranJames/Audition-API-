from init import db, ma

## Model 
#Actor Model
class Actor(db.Model):
     __tablename__ = "actors"

     id = db.Column(db.Integer, primary_key=True)
     f_name = db.Column(db.String, nullable=False)
     l_name = db.Column(db.String, nullable=False)
     agency = db.Column(db.String, nullable=False)
     ## Learn how to add FK here audition_id

## Actor Schema
class ActorSchema(ma.Schema):
    class Meta:
        model = Actor

    fields = ("f_name", "l_name", 'agency')    

audition_schema = ActorSchema()
audition_schema = ActorSchema(many=True)