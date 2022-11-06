from init import db, ma

#Role Model
class Role(db.Model):
     __tablename__ = "roles"

     id = db.Column(db.Integer, primary_key=True)
     role = db.Column(db.String, nullable=False)
     
     

## Role Schema
class RoleSchema(ma.Schema):
    class Meta:
        model = Role

    fields = ("role") 
    ordered = True