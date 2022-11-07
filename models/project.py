from init import db, ma

#Project Model
class Project(db.Model):
     __tablename__ = "projects"

     id = db.Column(db.Integer, primary_key=True)
     name = db.Column(db.String, nullable=False)
     director = db.Column(db.String, nullable=False)
     year = db.Column(db.String, nullable=False)
     ##Joining key to users table
     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
     user = db.relationship('User', back_populates ='projects')

## Project Schema
class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('name', 'director', 'year')
        ordered = True