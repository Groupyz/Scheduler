from flask import Blueprint, request
from log.log_handler import log
import response_handler

TASK_ROUTE = "/task"

# Create a Blueprint object
views_blueprint = Blueprint("views", __name__)


@views_blueprint.route("/")
@log
def hello():
    return "Hello, World!"


@views_blueprint.route(TASK_ROUTE, methods=["POST"])
@log
def task():
    return response_handler.post_task(request)
