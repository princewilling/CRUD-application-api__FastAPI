import pytest
from fastapi.testclient import TestClient
from app.db.database import Base, get_db
from app.main import app
from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 

SQLALCHEMY_DATABASE_URL = "postgresql://user :password@postgresserver/db"
#SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name} test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Testing_SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base.metadata.create_all(bind=engine) 

#Base = declarative_base()

# Dependency
# def override_get_db():
#     db = Testing_SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

#app.dependency_overrides[get_db] = override_get_db


#client = TestClient(app)

@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    db = Testing_SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
            
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)