from aiohttp import ClientSession

from app.core.redis.client import redis_client

from .dtos import (
    CountryInfoResponse,
    CountryInfoDTO,
)


class DaDataAPI:
    api_base_url: str = 'https://suggestions.dadata.ru/suggestions/api/4_1/rs/suggest'
    api_key: str = '928bdd5bfb829a3fad483136eeac0f499bbb8986'

    @property
    def http_headers(self) -> dict:
        return {
            'Authorization': f'Token {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    @staticmethod
    def _get_country_info_from_cache(
        country: str,
    ) -> CountryInfoDTO | None:
        redis_country_key = f'country_info_{country}'
        country_info_cache = redis_client.get(redis_country_key)

        if not country_info_cache:
            return None

        try:
            return CountryInfoDTO.parse_raw(country_info_cache)
        except Exception:
            return None

    @staticmethod
    def _save_country_data_to_cache(
        country: str,
        country_info: CountryInfoDTO,
    ) -> None:
        row_data = country_info.json()
        redis_client.set(f'country_info_{country}', row_data)

    async def _get_country_info_from_api(
        self,
        country: str,
    ) -> CountryInfoDTO | None:
        url = f'{self.api_base_url}/country'

        async with ClientSession(headers=self.http_headers) as session:
            async with session.post(
                url=url,
                json={'query': country},
            ) as resp:
                row_result = await resp.json()

            try:
                result = CountryInfoResponse.parse_obj(row_result)
            except Exception:
                return None

            return result.to_dto()

    async def get_country_info(
        self,
        country: str,
    ) -> CountryInfoDTO | None:
        country_info_cached = self._get_country_info_from_cache(country)
        if country_info_cached:
            return country_info_cached

        country_info_api = await self._get_country_info_from_api(country)
        if not country_info_api:
            return None

        self._save_country_data_to_cache(country, country_info_api)
        return country_info_api


dadata_api = DaDataAPI()
