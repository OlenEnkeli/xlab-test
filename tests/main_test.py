import pytest

from httpx import AsyncClient

from app.main import app


def validate_response(
    request: dict,
    response: dict,
) -> bool:
    for key, value in request.items():
        if (
            key not in response.keys()
            or response[key] != request[key]
        ):
            raise AssertionError(
                f'Value of {key} field is empty or not equal to request'
            )

    assert 'date_created' and 'date_modified' in response.keys()
    assert response['date_created'] is not None
    assert response['date_modified'] is not None


@pytest.mark.asyncio
async def test_main_api_flow():
    new_user_data = {
        'phone_number': '79954443321',
        'name': 'Ivan',
        'surname': 'Ivanov',
        'email': 'ivan.the.best@ivanov.mail',
        'patronymic': 'Ivanovich',
        'country': 'Норвегия',
    }

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.post(
            '/save_user_data',
            json=new_user_data,
        )

        assert response.status_code == 200
        validate_response(
            request=new_user_data,
            response=response.json(),
        )

        response = await client.get(
            '/get_user_data?phone_number=79954443321'
        )

        assert response.status_code == 200
        response_data = response.json()
        validate_response(
            request=new_user_data,
            response=response_data,
        )

        modify_time = response_data['date_modified']

        new_user_data['name'] = 'Petr'

        response = await client.post(
            '/save_user_data',
            json=new_user_data,
        )
        response_data = response.json()

        assert response.status_code == 200
        assert response_data['name'] == 'Petr'
        assert response_data['date_modified'] != modify_time

        response = await client.get(
            '/delete_user_data?phone_number=79954443321'
        )
        assert response.status_code == 200

        response = await client.get(
            '/get_user_data?phone_number=79954443321'
        )
        assert response.status_code == 404
