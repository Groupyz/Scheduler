import schedule


def post_task():
  print("1 -Hello, World!")
  job_that_executes_once()
  return 'Post task', 201


def job_that_executes_once():
    # Do some work that only needs to happen once...
    schedule.every(5).seconds.do(print_me, me="me!!!")
    return schedule.CancelJob

def print_me(me: str):
  print(me)