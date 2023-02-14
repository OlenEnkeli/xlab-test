from fastapi import APIRouter

from .endpoints import (
    user_data,
)


router = APIRouter()

router.include_router(user_data.router)
