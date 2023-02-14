import peewee

from app.core.db.manager import db


class BaseModel(peewee.Model):
    class Meta:
        database = db
