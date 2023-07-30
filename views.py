from flask import Blueprint, request
from log.log_handler import log
import request_handler

TASK_ROUTE = "/task"

# Create a Blueprint object
views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/")
@log
def hello():
    request_handler.job_that_executes_once()
    return "Hello, World!"


@views_blueprint.route(TASK_ROUTE, methods=["POST"])
@log
def task():
    return request_handler.post_task(request)
