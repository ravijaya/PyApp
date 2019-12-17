# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Define environment variable
ENV NAME World

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to install dependencies first
COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the source code
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]
