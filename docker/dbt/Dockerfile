# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy the dbt directory contents into the container at /usr/src/app/dbt
COPY ../dbt /usr/src/app/dbt

# Install any needed packages needed
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Install dbt
RUN pip install dbt-core && pip install dbt-postgres

# Add the cron schedule directly in the image
RUN echo "10 2 * * * cd /usr/src/app/dbt && /usr/src/app/dbt run" > /etc/cron.d/dbt-cron

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/dbt-cron

# Apply cron job
RUN crontab /etc/cron.d/dbt-cron

# Create the log file to be able to run tail
RUN touch /var/log/cron.log

# Expose any necessary ports
EXPOSE 80

# Run cron when the container launches
CMD cron