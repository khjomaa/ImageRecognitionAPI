# Use an official Python runtime as a parent image
FROM python:2.7

# Set the working directory to /app
WORKDIR /usr/src/app

COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Run app.py when the container launches
CMD ["python", "app.py"]
