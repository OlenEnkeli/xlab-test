from typing import List

from pydantic import BaseModel


class CountryInfoDTO(BaseModel):
    full_name: str
    short_name: str
    country_code: str
    alfa2: str
    alfa3: str


class CountryInfoData(BaseModel):
    code: str
    alfa2: str
    alfa3: str
    name_short: str
    name: str


class CountryInfoSuggestion(BaseModel):
    value: str
    data: CountryInfoData


class CountryInfoResponse(BaseModel):
    suggestions: List[CountryInfoSuggestion]

    def to_dto(self) -> CountryInfoDTO | None:
        if len(self.suggestions) == 0:
            return None

        return CountryInfoDTO(
            full_name=self.suggestions[0].data.name,
            short_name=self.suggestions[0].data.name_short,
            country_code=self.suggestions[0].data.code,
            alfa2=self.suggestions[0].data.alfa2,
            alfa3=self.suggestions[0].data.alfa3,
        )

