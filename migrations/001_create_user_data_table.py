from datetime import datetime as dt

import peewee

from peewee_migrate import Migrator


class UserData(peewee.Model):
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


def migrate(
    migrator: Migrator,
    database: peewee.Database,
    fake: bool = False,
    **kwargs,
):
    migrator.create_model(UserData)


def rollback(
    migrator: Migrator,
    database: peewee.Database,
    fake: bool = False,
    **kwargs,
):
    migrator.remove_model(UserData)
