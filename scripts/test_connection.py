import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# 1. Load the "Secret Keys" from your .env file
load_dotenv()

# 2. Get the credentials
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
db_name = os.getenv('DB_NAME')

# 3. Create the Connection String (The URL for your DB)
# format: postgresql://user:password@host:port/dbname
connection_url = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"

try:
    # 4. Try to connect
    engine = create_engine(connection_url)
    connection = engine.connect()
    print("Success! Python is now talking to the Medical Data Warehouse.")
    connection.close()
except Exception as e:
    print(f"Connection Failed. Error: {e}")