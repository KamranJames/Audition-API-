from init import db, ma


## Casting Model
class Casting(db.Model):
     __tablename__ = "castings"

     id = db.Column(db.Integer, primary_key=True)
     ## cd is short for casting director
     cd = db.Column(db.String, nullable=False)
     location = db.Column(db.String, nullable=False)

## Casting Schema
class CastingSchema(ma.Schema):
    class Meta:
       ##model = Casting
       ##cd is short for casting director
       fields = ("cd", "location",)
       ordered = True