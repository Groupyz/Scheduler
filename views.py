from main import app
from main import schedule

# Define a route for the home page
@app.route('/')
def hello_world():
    print("1 -Hello, World!")
    job_that_executes_once()
    print("2 - Hello, World!")
    return 'Hello, World!'


def job_that_executes_once():
    # Do some work that only needs to happen once...
    schedule.every(5).seconds.do(print_me, me="me!!!")
    return schedule.CancelJob

def print_me(me: str):
  print(me)