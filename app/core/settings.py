from pydantic import AnyHttpUrl, BaseSettings


class Settings(BaseSettings):

    API_STATUS: str

    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    SERVER_TZ: str

    PROJECT_NAME: str
    PROJECT_VERSION: str

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    REDIS_HOST: str
    REDIS_PORT: str
    REDIS_DB: str

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()


LOG_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
        'colored': {
            '()': 'coloredlogs.ColoredFormatter',
            'format': "%(asctime)s (%(levelname)s) %(name)s %(message)s"
        },
        "default": {"format": "%(asctime)s [%(process)s] %(levelname)s: %(message)s"}
    },
    "handlers": {
        "console": {
            "formatter": "colored",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout"
        }
    },
    "root": {"handlers": ["console"]},
    "loggers": {
        "gunicorn": {"propagate": True},
        "gunicorn.access": {"propagate": True},
        "gunicorn.error": {"propagate": True},
        "uvicorn": {"propagate": True},
        "uvicorn.access": {"propagate": True},
        "uvicorn.error": {"propagate": True},
    }
}

