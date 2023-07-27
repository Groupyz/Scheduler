import schedule
from flask import request, jsonify
import json


def post_task(request: request):
  return_data = None

  if not request.is_json:
    return_data = jsonify({"error": "Invalid request data format. Expected JSON."}), 400
  else:
    json_data = jsonify({"test": ""}), 201
    print("1 -Hello, World!")
    job_that_executes_once()

  json_data = json.dumps(return_data)
  return json_data


def job_that_executes_once():
    # Do some work that only needs to happen once...
    schedule.every(5).seconds.do(print_me, me="me!!!")
    return schedule.CancelJob

def print_me(me: str):
  print(me)

