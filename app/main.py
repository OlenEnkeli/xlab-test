
import logging
import logging.config

from fastapi import FastAPI

import coloredlogs

from app.core.settings import settings, LOG_CONFIG
from app.api.router import router


coloredlogs.install()
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)

logger.info(f'Swagger url: {settings.SERVER_HOST}/docs/')
logger.info(f'Redoc url: {settings.SERVER_HOST}/redoc/')


app = FastAPI(
    title=settings.PROJECT_NAME,
)

app.include_router(router)
