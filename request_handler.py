from scheduler_wrapper import scheduler
from flask import request, jsonify
from validator import validate_pipeline, is_json, post_task_has_needed_data

post_is_valid = validate_pipeline([is_json, post_task_has_needed_data])


def post_task(request: request):
    json_data = None
    if post_is_valid(request):
        json_data = jsonify({"message": "Task received successfully"}), 201
    else:
        json_data = jsonify({"message": "Invalid request."}), 400

    return json_data
