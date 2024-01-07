# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install cron
RUN apt-get update && apt-get install -y cron

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Add cron job to schedule script execution
RUN echo "0 2 * * * /usr/local/bin/python /usr/src/app/scripts/ingest_data.py" > /etc/crontab

# Run cron in the foreground
CMD ["cron", "-f"]