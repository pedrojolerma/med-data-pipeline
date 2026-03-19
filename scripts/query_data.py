import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

# Connect to the DB
conn_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(conn_string)

# Run a SQL Query
query = "SELECT * FROM imaging_metadata WHERE modality = 'MRI';"

try:
    print("--- Running Database Query: All MRI Scans ---")
    df_results = pd.read_sql(query, engine)
    print(df_results)
except Exception as e:
    print(f"Query Failed: {e}")