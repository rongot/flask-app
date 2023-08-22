from sqlalchemy.sql import func
from . import db
from . import ma
import datetime

class Articals(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100))
    body=db.Column(db.Text())
    date=db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self,title,body):
        self.title=title
        self.body=body

class ArticalsSchema(ma.Schema):
    class Meta:
        fields=('id','title','body','date')