import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

# 1. Connect to the DB
conn_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(conn_string)

# 2. Read the Medical CSV
print("Reading CSV data...")
df = pd.read_csv('data/imaging_records.csv')

# 3. Load into SQL
try:
    # 'if_exists=append' adds new data without deleting the table
    # 'index=False' prevents Pandas from creating a separate ID column
    df.to_sql('imaging_metadata', engine, if_exists='append', index=False)
    print(f"Success! {len(df)} records loaded into the 'imaging_metadata' table.")
except Exception as e:
    print(f"Ingestion Failed: {e}")