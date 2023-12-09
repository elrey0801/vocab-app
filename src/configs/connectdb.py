from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import logging
from configs.configLogging import configLogging
configLogging()
logger = logging.getLogger(__name__)

dotenv_path = os.path.join(os.path.dirname(__file__), '..\..', '.env')
load_dotenv(dotenv_path)


# DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
DATABASE_URL = f"mysql+mysqlconnector://remote:Tung%4021061996@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
logger.info('---' + DATABASE_URL)
engine = None
Base = declarative_base()
try:
    # engine = create_engine(DATABASE_URL, echo=True)
    engine = create_engine(DATABASE_URL, echo=False)
    if not database_exists(engine.url):
        create_database(engine.url)
        logger.info('---New DB created')
    else:
    # Connect the database if exists.
        engine.connect()
        logger.info('---Connect DB:: OK')
except Exception as error:
    logger.error('---Connect DB:: Failed')
    logger.error(error)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

