import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection string (make sure PostgreSQL is running and configured correctly)
DATABASE_URL = "postgresql://username:password@localhost:5432/etl_db"

# Step 1: Extract - Load data from CSV
def extract_data(csv_file):
    try:
        data = pd.read_csv(csv_file)
        print("Data extracted successfully")
        return data
    except Exception as e:
        print("Error extracting data:", e)

# Step 2: Transform - Clean the data
def transform_data(data):
    data.dropna(subset=['age', 'email'], inplace=True)  # Drop rows with missing age or email
    print("Data transformed successfully")
    return data

# Step 3: Load - Load data into PostgreSQL
def load_data(data):
    engine = create_engine(DATABASE_URL)
    try:
        data.to_sql('users', engine, if_exists='replace', index=False)
        print("Data loaded successfully")
    except Exception as e:
        print("Error loading data:", e)

if __name__ == "__main__":
    # Ensure CSV file exists
    if not os.path.isfile('data.csv'):
        print("CSV file not found!")
    else:
        # Run ETL pipeline
        data = extract_data('data.csv')
        data = transform_data(data)
        load_data(data)
