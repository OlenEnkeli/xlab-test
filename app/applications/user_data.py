from app.core.db.manager import manager
from app.schemas.user_data import (
    UserDataResponse,
    UserDataRequest,
)
from app.models.user_data import UserData
from app.services.dadata.api import dadata_api


class UserDataController:
    async def _get_by_phone_number(
        self,
        phone_number: str,
    ) -> UserData | None:
        try:
            return await manager.get(
                UserData,
                UserData.phone_number == phone_number,
            )
        except Exception:
            return None

    async def get_by_phone_number(
        self,
        phone_number: str,
    ) -> UserDataResponse | None:
        model = await self._get_by_phone_number(phone_number=phone_number)
        if not model:
            return None

        country_info = await dadata_api.get_country_info(country=model.country)

        return UserDataResponse(
            phone_number=model.phone_number,
            name=model.name,
            surname=model.surname,
            patronymic=model.patronymic,
            email=model.email,
            country=model.country,
            country_code=country_info.country_code if country_info else None,
            id=model.id,
            date_created=model.date_created,
            date_modified=model.date_modified,
        )

    async def create_or_update(
        self,
        origin: UserDataRequest,
    ) -> None:
        existed_model = await self._get_by_phone_number(origin.phone_number)

        if existed_model:
            model = UserData(
                id=existed_model.id,
                **origin.dict(),
            )

            await self.get_by_phone_number(model.phone_number)

        else:
            await manager.create(
                UserData,
                **origin.dict(),
            )

    async def delete(
        self,
        phone_number: str,
    ) -> bool:
        existed_model = await self._get_by_phone_number(phone_number=phone_number)

        if not existed_model:
            return False
        try:
            await manager.delete(existed_model)
        except Exception as e:
            return False

        return True


user_data_controller = UserDataController()
