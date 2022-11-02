from init import db, ma

#Project Model
class Project(db.Model):
     __tablename__ = "projects"

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String, nullable=False)
     director = db.Column(db.String, nullable=False)
     year = db.Column(db.String, nullable=False)
     ## Learn how to add FK here audition_id

## Project Schema
class ProjectSchema(ma.Schema):
    class Meta:
        model = Project

    fields = ("name", "director", 'year') 

Project_schema = ProjectSchema()
Project_schema = ProjectSchema(many=True)