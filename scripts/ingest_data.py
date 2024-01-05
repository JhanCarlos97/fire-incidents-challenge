import os
import requests
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define the PostgreSQL connection parameters
db_params = {
    'host': os.getenv('POSTGRES_HOST'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'database': os.getenv('POSTGRES_DB'),
}

# Read the SQL statement from the file
with open('insert_raw_incidents_data.sql', 'r') as sql_file:
    insert_sql = sql_file.read()

# Fetch data from the API endpoint
api_url = 'https://data.sfgov.org/resource/wr8u-xric.json'
response = requests.get(api_url)
data = response.json()

# Connect to the PostgreSQL database
conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Iterate through the data and insert into the PostgreSQL table
for record in data:
    # Perform any necessary transformations here
    # For example, converting date strings to timestamps

    # Insert data into the PostgreSQL table
    cursor.execute(insert_sql, (record['date'], record['district'], record['battalion'], ...))

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()