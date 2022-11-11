from init import db, ma
from marshmallow import fields
from marshmallow.validate import Length

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    date = db.Column(db.Date) # Date created

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

    user = db.relationship("User", back_populates="comments")
    projects = db.relationship("Project", back_populates="comments")


class CommentSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['name', 'email'])
    project = fields.Nested('ProjectSchema')
    message = fields.String(required=True, validate=Length(min=1, max=50, error='message must be at least 1 character min and 50 characters max'))

    class Meta:
        fields = ('id', 'message', 'date', 'project', 'user')
        ordered = True