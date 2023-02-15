from peewee_async import PostgresqlDatabase, Manager

from app.core.settings import settings


db = PostgresqlDatabase(
    settings.POSTGRES_DB,
    {
        'host': settings.POSTGRES_SERVER,
        'user': settings.POSTGRES_USER,
        'password': settings.POSTGRES_PASSWORD
    }
)

db.set_allow_sync(False)
manager = Manager(db)
