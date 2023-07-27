import pytest
from app import app
from views import job_that_executes_once, TASK_ROUTE


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_task_endpoint(client, mocker):
    # Mock the behavior of schedule.every().seconds.do() to avoid scheduling the job
    mocker.patch('schedule.every')

    # Call the job_that_executes_once directly to simulate the scheduler job
    job_that_executes_once()

    # Send a POST request to '/task' with empty JSON data
    response = client.post(TASK_ROUTE, json={})

    # Assert the response status code and content
    assert response.status_code == 201
    assert response.get_json() == {"message": "Task received successfully"}

    # Assert that job_that_executes_once() was called
    schedule.every.assert_called_once_with(5)

def test_task_valid_post(client):
    """Test the '/task' route."""
    # Prepare the JSON data to send with the request
    json_data = message_data_json_dummy()

    # Make a POST request to the '/task' route
    response = client.post(TASK_ROUTE, json=json_data)

    # Check the response status code and message
    assert response.status_code == 201
    assert response.json['message'] == "Task received successfully"


def test_task_route_missing_data(client):
    """Test the '/task' route with missing data."""
    missing_attribute = 'group_ids'
    json_data = message_data_json_dummy()
    del json_data[missing_attribute]

    # Make a POST request to the '/task' route
    response = client.post(TASK_ROUTE, json=json_data)

    # Check the response status code and message
    assert response.status_code == 400
    assert response.json['message'] == "The {missing_attribute} attribute is missing in the input to create a task."

def test_task_route_accepts_post(client):
    response = client.post(TASK_ROUTE)
    assert response.status_code == 201

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