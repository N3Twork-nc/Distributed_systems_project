# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the test_kafka.py file to the working directory
COPY test_kafka.py .

# Set the command to run when the container starts
CMD ["python", "test_kafka.py"]