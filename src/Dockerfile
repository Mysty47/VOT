# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir Flask minio flask-jwt-extended python-keycloak boto3

# Expose the port Flask will run on
EXPOSE 5000

# Define the default command to run your app
CMD ["python", "app.py"]
