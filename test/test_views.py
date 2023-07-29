import pytest
import schedule
from app import app
from views import TASK_ROUTE
from request_handler import job_that_executes_once


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_task_endpoint(client, mocker):
    mocker.patch('schedule.every')

    response = client.post(TASK_ROUTE, json=message_data_json_dummy())

    assert response.status_code == 201
    assert response.get_json() == {"message": "Task received successfully"}
    schedule.every.assert_called_once_with(5)

def test_task_valid_post(client):
    """Test the '/task' route."""
    json_data = message_data_json_dummy()

    response = client.post(TASK_ROUTE, json=json_data)

    assert response.status_code == 201
    assert response.json['message'] == "Task received successfully"


def test_task_route_missing_data(client):
    """Test the '/task' route with missing data."""
    missing_attribute = 'group_ids'
    json_data = message_data_json_dummy()
    del json_data[missing_attribute]

    response = client.post(TASK_ROUTE, json=json_data)

    assert response.status_code == 400
    assert response.json.get('message') == "Invalid request."

def test_hello_world():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Hello, World!'



def message_data_json_dummy(**kwargs) -> dict:
    dummy_data = {
        "user_id": "342342fsd",
        "group_ids": ["sdfds", "2131fsdf"],
        "message_data": "test data",
        "time_to_send": "yyyy-MM-dd"
    }
    dummy_data.update(kwargs)

    return dummy_data