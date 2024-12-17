# Use an official Python runtime as the base image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and templates into the container
COPY app.py .
COPY templates/ templates/

# Make port 5000 available outside the container
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
