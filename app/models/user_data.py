from datetime import datetime as dt

import peewee

from app.core.db.base import BaseModel


class UserData(BaseModel):
    phone_number = peewee.CharField(
        unique=True,
        index=True,
        max_length=12,
    )
    name = peewee.CharField(
        max_length=50,
    )
    surname = peewee.CharField(
        max_length=50,
    )
    email = peewee.CharField(
        max_length=50,
        null=True,
    )
    patronymic = peewee.CharField(
        null=True,
    )
    country = peewee.CharField(
        max_length=50,
    )

    date_created = peewee.DateTimeField(
        default=dt.now,
    )
    date_modified = peewee.DateTimeField(
        default=dt.now,
    )