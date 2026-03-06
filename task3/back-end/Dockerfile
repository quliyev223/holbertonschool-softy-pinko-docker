# Use the latest Ubuntu image
FROM ubuntu:latest

# Update package list and install Python and Pip
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y python3 python3-pip

# Install Flask and Flask-CORS
# We need Flask-CORS to allow the front-end to talk to this API
RUN pip3 install flask flask-cors

# Set the working directory inside the container
WORKDIR /app

# Copy the python script into the container
COPY ./api.py /app/api.py

# Run the flask application
CMD ["python3", "/app/api.py"]
