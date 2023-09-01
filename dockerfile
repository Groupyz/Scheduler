# Use the official Python image as the base image
FROM python:3.11.3

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose the port that Flask will run on (change it if needed)
EXPOSE 5003

# Run the Flask application
CMD [ "flask", "run", "--host=0.0.0.0", "--port=5053"]