import os
import psycopg2
from dotenv import load_dotenv

def connect_to_postgre():

    # Load environment variables from .env file
    load_dotenv()

    # Define the PostgreSQL connection parameters
    db_params = {
        'host': 'postgres',
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
        'database': os.getenv('POSTGRES_DB'),
        'port': os.getenv('POSTGRES_PORT')
    }

    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)

    return conn