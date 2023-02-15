from fastapi import (
    APIRouter,
    HTTPException,
    Depends,
)

from app.schemas.user_data import (
    UserDataResponse,
    UserDataRequest,
)
from app.applications.user_data import user_data_controller as controller


router = APIRouter()


@router.get(
    '/get_user_data',
    response_model=UserDataResponse,
)
async def get_user_data(phone_number: str) -> UserDataResponse:
    result = await controller.get_by_phone_number(phone_number=phone_number)

    if not result:
        raise HTTPException(
            status_code=404,
            detail={'not_found_user_data': {
                'phone_number': phone_number
            }}
        )

    return result


@router.post(
    '/save_user_data',
    response_model=UserDataResponse,
)
async def save_user_data(user_data: UserDataRequest):
    await controller.create_or_update(origin=user_data)
    return await controller.get_by_phone_number(phone_number=user_data.phone_number)


@router.get(
    '/delete_user_data',
)
async def delete_user_data(phone_number: str) -> dict:
    result = await controller.delete(phone_number=phone_number)

    if not result:
        raise HTTPException(
            status_code=404,
            detail={'not_found_user_data': {
                'phone_number': phone_number
            }}
        )

    return {'success': 'ok'}
