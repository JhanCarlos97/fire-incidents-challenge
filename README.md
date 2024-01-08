# Fire Incidents Data Analysis

## Overview

This repository provides a simple Python script and Docker setup to facilitate the analysis of fire incidents data in the city of San Francisco. The script fetches the data from San Francisco Fire Incidents API, connects to a local PostgreSQL database, ingest it into a main raw table called `raw_incidents` and then, four tables/views are generated in the `test_rendered_models` schema via `dbt run` command, and displays the results in a Python Notebook at the `notebooks` folder. These tables represent aggregated incidents along the dimensions of time period, district, and battalion.

## Data Source and Ingestion

The fire incidents data is sourced from the [San Francisco Fire Incidents API](https://data.sfgov.org/Public-Safety/Fire-Incidents/wr8u-xric/about_data). The data is ingested into the local PostgreSQL database every day, ensuring that the analysis reflects the most recent information available.

## Prerequisites

Before running the script, ensure you have the following:

- Docker installed
- Python 3.x installed
- Required Python packages: `psycopg2-binary` and `python-dotenv`. Install them using:

  ```bash
  pip install psycopg2-binary python-dotenv

## Test Locally

To test the project locally, follow these steps:

1. Start the local environment using Docker Compose, by being placed at the `docker/` folder:

   ```bash
   docker-compose up

2. Run the ingestion script to fetch data from the SF API and populate the local database:

   ```bash
   docker-compose run cron python scripts/ingest_data.py

Run the ingestion script a second time to verify that there is no new data.

If there is no new data, the script will output "No new data"

3. Use dbt to create models/views from the ingested data:

   ```bash
   docker-compose run dbt sh -c "cd /usr/src/app/dbt && dbt run"
  
4. Explore the data using the provided Jupyter Notebook in the "notebooks" folder.

## Adding New Models

To add new models or SQL queries, simply create them in the `dbt/models` directory. When you run the dbt run command again, dbt will automatically update the existing models and create any new ones.

Feel free to customize the instructions based on your specific project structure and requirements.

## Project Status

This project was developed to address specific requirements within a given timeframe. While the main focus was on delivering a functional solution, there are areas for potential improvement in code quality and structure.

### Areas for Improvement

- Code Structure: The current organization meets the immediate requirements but may benefit from refactoring to enhance readability and maintainability.
- Documentation: The project strives to provide clear and concise documentation; however, there's room for improvement in the depth and coverage of code comments and explanations.

### Consideration for Timely Delivery

Given the nature of the project and the specified timeframe, the primary goal was to deliver a working solution. Appreciation is extended for understanding this approach, and any feedback or suggestions for improvement are welcomed.

Contributions and feedback are appreciated to help enhance the project further. Insights and recommendations are valuable, and the project is open to making refinements based on those suggestions.