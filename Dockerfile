# Use the slim Python image as the base
FROM python:3.10.12-slim

# Install system dependencies needed for building
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
 && rm -rf /var/lib/apt/lists/*

# Set up the working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Command to run the Python script
CMD ["python3", "main1.py"]
