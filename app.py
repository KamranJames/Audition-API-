from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
##db= SQLAlchemy(app)

##app.config ['JSON_SORT_KEYS'] = False
##app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
##app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
##app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

@app.route('/')
def index():
    return "Hello world"

class Audition(db.model):
     __tablename__ = "auditions"

     audition_id = db.Column(db.Integer, primary_key=True)
     project = db.Column(db.String, nullable=False)
     date = db.Column(db.Date, nullable=False)
     comments = db.Column(db.string)

     #learn how to join the FK below with the assosciated models.
     ##Fk casting_director_id
     ##Fk actor_id

class Casting(db.model):
     __tablename__ = "castings"

     casting_id = db.Column(db.Integer, primary_key=True)
     director = db.Column(db.String, nullable=False)
     location = db.Column(db.String, nullable=False)


class Actor(db.model):
     __tablename__ = "actors"

     actor_id = db.Column(db.Integer, primary_key=True)
     f_name = db.Column(db.String, nullable=False)
     l_name = db.Column(db.String, nullable=False)
     agency = db.Column(db.String, nullable=False)
     ## Learn how to add FK here audition_id


## SCHEMAS 

## Audition Schema 
class AuditionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Audition

    fields = ("project", "date", "comments")    

audition_schema = AuditionSchema()
audition_schema = AuditionSchema(many=True)

## Casting Schema
class CastingSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Casting
        
    fields = ("director", "location",)    

casting_schema = CastingSchema()
casting_schema = CastingSchema(many=True)

## Acting Schema
class ActorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Actor

    fields = ("f_name", "l_name", 'agency')    

audition_schema = ActorSchema()
audition_schema = ActorSchema(many=True)
