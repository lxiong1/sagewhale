import pytest


@pytest.fixture
def db_mock(mocker):
    return mocker.Mock()


@pytest.fixture
def file_content():
    return [
        {
            "id": "4657e1b3-9dfa-4dce-90a1-0248a5edb974",
            "first_name": "Tabbitha",
            "last_name": "Lorden",
            "full_name": "Tabbitha Lorden",
            "demographics": {
                "id": "29d8a410-bbce-487e-bc69-5e2d64a4b2e3",
                "gender": "Female",
                "age": 54,
                "race": "Hmong",
                "marital_status": "Divorced",
                "education": "Bachelor degree",
                "household_income": "40000-49999",
            },
            "email_performance": {
                "id": "9aeef2c8-3c54-4d5f-8788-42ace39b3425",
                "products": [
                    {
                        "id": "6746bf9b-6fbd-4fa4-a1e8-f5350d62e02c",
                        "product_type": "Clothing",
                        "total_send_rate": 277,
                        "total_open_rate": 195,
                    }
                ],
            },
        }
    ]
