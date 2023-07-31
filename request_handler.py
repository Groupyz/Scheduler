from scheduler_wrapper import scheduler
import datetime
from flask import request, jsonify
from validator import validate_pipeline, is_json, post_task_has_needed_data

post_is_valid = validate_pipeline([is_json, post_task_has_needed_data])


def post_task(request: request):
    json_data = None
    if post_is_valid(request):
        run_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
        scheduler.add_job(print_hello_world, "date", run_date=run_time)
        json_data = jsonify({"message": "Task received successfully"}), 201
    else:
        json_data = jsonify({"message": "Invalid request."}), 400

    return json_data


def print_hello_world():
    print("Hello, World!")
