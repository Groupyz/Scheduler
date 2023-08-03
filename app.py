from scheduler_wrapper import scheduler
from flask import Flask
from views import views_blueprint
from log.log_handler import init_logger

# Create a Flask app
app = Flask(__name__)
app.register_blueprint(views_blueprint)


if __name__ == "__main__":
    init_logger()

    # Run the Flask app on localhost with port 5000
    app.run(host="localhost", port=5050)
