# Use the latest Ubuntu image as the foundation
FROM ubuntu:latest

# Update the package list and install python3 and pip3
# The -y flag automatically confirms installation
RUN apt-get update && apt-get install -y python3 python3-pip

# Remove this file to avoid "externally-managed-environment" errors when using pip
RUN rm /usr/lib/python*/EXTERNALLY-MANAGED

# Install Flask using pip3 as required
RUN pip3 install flask

# Set the working directory inside the container to /app
WORKDIR /app

# Copy our Python script from the local directory to the container
COPY ./api.py /app/api.py

# Command to run the Flask application
CMD ["python3", "api.py"]
