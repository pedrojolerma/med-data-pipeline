import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

# Build the connection string
conn_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
engine = create_engine(conn_string)

# Read the SQL file we just created
with open('sql/create_tables.sql', 'r') as f:
    sql_command = f.read()

try:
    with engine.connect() as conn:
        conn.execute(text(sql_command))
        conn.commit()
        print("Table 'imaging_metadata' created successfully!")
except Exception as e:
    print(f"SQL Execution Failed: {e}")