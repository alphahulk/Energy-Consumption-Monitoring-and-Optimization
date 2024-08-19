import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# Generate synthetic energy consumption data
def generate_data(num_records):
    data = []
    for _ in range(num_records):
        record = {
            'meter_id': fake.uuid4(),
            'timestamp': fake.date_time_this_year(),
            'energy_consumption': round(np.random.uniform(0.5, 5.0), 2)
        }
        data.append(record)
    return pd.DataFrame(data)

# Generate 10,000 records of synthetic data
df = generate_data(10000)
print(df.head())



import psycopg2
from psycopg2.extras import execute_values

# Database connection details
db_params = {
    'dbname': 'oftzglhs',
    'user': 'oftzglhs',
    'password': 'SJhdGxk_-kk6Ss0UlYOwhvmtfGJioAYX',
    'host': 'kashin.db.elephantsql.com',
    'port': 5432
}

# Convert DataFrame to a list of tuples
data_tuples = [tuple(x) for x in df.to_numpy()]

# SQL query to insert data
insert_query = """
INSERT INTO energy_consumption (meter_id, timestamp, energy_consumption)
VALUES %s
"""

# Function to insert data into PostgreSQL
def insert_data(data):
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(**db_params)
        cur = conn.cursor()
        
        # Insert data using execute_values for batch insert
        execute_values(cur, insert_query, data)
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cur.close()
        conn.close()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Insert data into the database
insert_data(data_tuples)
