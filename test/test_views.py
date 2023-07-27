import pytest
from app import app
from views import job_that_executes_once


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
    response = client.post('/task', json={})

    # Assert the response status code and content
    assert response.status_code == 200
    assert response.get_json() == {"message": "Task received successfully"}

    # Assert that job_that_executes_once() was called
    schedule.every.assert_called_once_with(5)