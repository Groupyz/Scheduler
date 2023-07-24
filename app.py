import threading
import time
import schedule
from flask import Flask
from views import views_blueprint

# Create a Flask app
app = Flask(__name__)
app.register_blueprint(views_blueprint)

# Function to run the scheduler in a separate thread
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # Start the background task thread
    bg_thread = threading.Thread(target=run_scheduler)
    bg_thread.daemon = True
    bg_thread.start()

    # Run the Flask app on localhost with port 5000
    app.run(host='localhost', port=5000)
