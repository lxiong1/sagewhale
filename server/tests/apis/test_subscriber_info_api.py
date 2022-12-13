import json
from io import BytesIO
from http import HTTPStatus
import pytest
from sagewhale import app


def describe_get():
    def test_should_retrieve_all_subscriber_info(test_client):
        response = test_client.get(
            "/subscriber_info",
            content_type="application/json",
        )

        assert response.status_code == HTTPStatus.OK


def describe_post():
    def test_should_upload_json_file(test_client, file_content):
        file_content_string = json.dumps(file_content)
        data = {"file": (BytesIO(bytes(file_content_string, "utf-8")), "file.json")}

        response = test_client.post(
            "/subscriber_info/upload/json",
            data=data,
            content_type="multipart/form-data",
        )

        assert response.status_code == HTTPStatus.CREATED

    def test_should_respond_with_error_when_payload_not_file(test_client):
        response = test_client.post(
            "/subscriber_info/upload/json",
            data="{}",
            content_type="application/json",
        )

        assert "Input payload validation failed" in response.data.decode()

    def test_should_respond_with_error_when_file_is_not_json(test_client):
        non_json_file = "file.csv"
        data = {"file": (BytesIO(b"some_file_content"), non_json_file)}

        response = test_client.post(
            "/subscriber_info/upload/json",
            data=data,
            content_type="multipart/form-data",
        )

        assert "Requires JSON file" in response.data.decode()


@pytest.fixture
def test_client():
    app.config["TESTING"] = True

    with app.app_context():
        with app.test_client() as client:
            yield client
