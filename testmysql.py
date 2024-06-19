from sqlalchemy import create_engine
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)

try:
    connection = engine.connect()
    print("Database connection successful!")
    connection.close()
except Exception as e:
    print(f"Database connection failed: {e}")
