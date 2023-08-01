import time
import datetime
import pytest
from app import app
from views import TASK_ROUTE
from test_views import message_data_json_dummy
import requests
import requests_mock

BOT_URL_POST_MESSAGE = "http://example.com/api_endpoint"


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def api_url():
    return BOT_URL_POST_MESSAGE


def test_task_endpoint(client, capsys):
    run_time = datetime.datetime.now() + datetime.timedelta(seconds=3)
    formatted_string = run_time.strftime("%Y-%m-%d %H:%M:%S")
    json_data = message_data_json_dummy(time_to_send=formatted_string)
    response = client.post(TASK_ROUTE, json=json_data)
    assert response.status_code == 201

    time.sleep(5)
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out


# def test_post_request(api_url, mocker):
#     json_data = message_data_json_dummy()

#     # Mock the response with status code 200 and a custom JSON body
#     with requests_mock.Mocker() as m:
#         m.post(api_url, status_code=200, json={"message": "success"})

#         # Send the POST request with dummy data
#         response = requests.post(api_url, json=json_data)
#         response = post_message(json_data)

#         # Check if the status code is 200
#         assert (
#             response.status_code == 200
#         ), f"Expected status code 200, but received {response.status_code}"

#         # Verify that the request was made exactly once
#         assert m.called_once
