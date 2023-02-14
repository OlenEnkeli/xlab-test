from typing import Self, Any
from datetime import datetime as dt

from pydantic import BaseModel, Field, validator


class UserData(BaseModel):
    phone_number: str = Field(
        ...,
        max_length=12,
    )

    name: str = Field(
        ...,
        max_length=50,
    )
    surname: str = Field(
        ...,
        max_length=50,
    )
    email: str = Field(
        ...,
        max_length=50,
    )
    patronymic: str = Field(
        None,
        max_length=50,
    )
    country: str = Field(
        ...,
        max_length=50,
    )

    @validator('phone_number')
    def validate_phone_number(
        cls: Self,
        value: str,
    ) -> Self:
        if not (
            value[0] == '7' or
            value[0:2] == '+7'
        ):
            raise ValueError(
                'Phone number must start with 7 or +7'
            )

        return value


class UserDataResponse(UserData):
    user_id: int = Field(
        ...,
        alias='id',
    )

    date_created: dt = dt.now()
    date_modified: dt = dt.now()


class UserDataRequest(UserData):
    pass
