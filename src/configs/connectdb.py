from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '../..', '.env')
load_dotenv(dotenv_path)

DATABASE_URL = f"mysql+mysqlconnector://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
print(DATABASE_URL)
try:
    engine = create_engine(DATABASE_URL, echo=True)
    print('Connect DB:: OK')
except:
    print('Connect DB:: Failed')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()