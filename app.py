from flask import Flask, jsonify, request 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://audition.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
##app.config ['JSON_SORT_KEYS'] = False
##app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
##app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

db = SQLAlchemy(app)
ma = Marshmallow()


@app.route('/')
def index():
    return "Hello world"

class Audition(db.Model):
     __tablename__ = "auditions"

     audition_id = db.Column(db.Integer, primary_key=True)
     project = db.Column(db.String, nullable=False)
     date = db.Column(db.Date, nullable=False)
     comments = db.Column(db.String)

     #learn how to join the FK below with the assosciated models.
     ##Fk casting_director_id
     ##Fk actor_id

class Casting(db.Model):
     __tablename__ = "castings"

     casting_id = db.Column(db.Integer, primary_key=True)
     director = db.Column(db.String, nullable=False)
     location = db.Column(db.String, nullable=False)


class Actor(db.Model):
     __tablename__ = "actors"

     actor_id = db.Column(db.Integer, primary_key=True)
     f_name = db.Column(db.String, nullable=False)
     l_name = db.Column(db.String, nullable=False)
     agency = db.Column(db.String, nullable=False)
     ## Learn how to add FK here audition_id


## SCHEMAS 

## Audition Schema 
class AuditionSchema(ma.Schema):
    class Meta:
        model = Audition

    fields = ("project", "date", "comments")    

audition_schema = AuditionSchema()
audition_schema = AuditionSchema(many=True)

## Casting Schema
class CastingSchema(ma.Schema):
    class Meta:
        model = Casting
        
    fields = ("director", "location",)    

casting_schema = CastingSchema()
casting_schema = CastingSchema(many=True)

## Acting Schema
class ActorSchema(ma.Schema):
    class Meta:
        model = Actor

    fields = ("f_name", "l_name", 'agency')    

audition_schema = ActorSchema()
audition_schema = ActorSchema(many=True)


@app.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")