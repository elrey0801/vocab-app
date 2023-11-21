from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..\..', '.env')
# print('DB::', dotenv_path)
load_dotenv(dotenv_path)

DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
print(DATABASE_URL)
engine = None
Base = declarative_base()
try:
    engine = create_engine(DATABASE_URL, echo=True)
    if not database_exists(engine.url):
        create_database(engine.url)
        print('New DB created')
    else:
    # Connect the database if exists.
        engine.connect()
        print('Connect DB:: OK')
except Exception as error:
    print('Connect DB:: Failed', error)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

