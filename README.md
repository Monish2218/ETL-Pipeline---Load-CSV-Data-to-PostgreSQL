# ETL Pipeline: CSV to PostgreSQL

## Overview
This project demonstrates a simple ETL pipeline in Python that extracts data from a CSV, cleans it, and loads it into a PostgreSQL database.

## Steps
1. **Extract**: Loads data from a CSV file.
2. **Transform**: Cleans the data by removing rows with missing age or email.
3. **Load**: Inserts data into a PostgreSQL table named `users`.

## Requirements
- Python 3.x
- PostgreSQL
- Python packages: `pandas`, `sqlalchemy`

## Usage
1. Update `DATABASE_URL` in the code with your PostgreSQL credentials.
2. Run `etl_csv_to_postgres.py`.

