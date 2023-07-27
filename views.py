import schedule
from flask import Blueprint
from log.log_handler import log

TASK_ROUTE = '/task'

# Create a Blueprint object
views_blueprint = Blueprint('views', __name__)


@views_blueprint.route('/')
@log
def hello():
    print("1 -Hello, World!")
    job_that_executes_once()
    print("2 - Hello, World!")
    return 'Hello, World!'

@views_blueprint.route(TASK_ROUTE, methods=['POST'])
@log
def task():
    print("1 -Hello, World!")
    job_that_executes_once()
    return 'Post task', 201

def job_that_executes_once():
    # Do some work that only needs to happen once...
    schedule.every(5).seconds.do(print_me, me="me!!!")
    return schedule.CancelJob

def print_me(me: str):
  print(me)