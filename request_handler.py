import schedule
from flask import request, jsonify
from validator import validate_pipeline, is_json, post_task_has_needed_data

post_is_valid = validate_pipeline([is_json, post_task_has_needed_data])



def post_task(request: request):
  json_data = None
  if post_is_valid(request):
    json_data = jsonify({"message": "Task received successfully"}), 201
    print("1 -Hello, World!")
    job_that_executes_once()
  else:
    json_data = jsonify({"message": "Invalid request."}), 400

  return json_data


def job_that_executes_once():
    # Do some work that only needs to happen once...
    schedule.every(5).seconds.do(print_me, me="me!!!")
    return schedule.CancelJob

def print_me(me: str):
  print(me)
