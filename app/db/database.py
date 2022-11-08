import time
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
    
# while True:
#     try:
#         # Connect to your postgres DB
#         conn = psycopg2.connect(host='localhost', 
#                                 database='fastapi crud system', user='princewillingoo', 
#                                 password="1234", 
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Succesfully Connected To DB")
#         break
#     except Exception as error:
#         print("Failed To Connect DB")
#         print(error)
#         time.sleep(3)
