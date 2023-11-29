import logging
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '..\..', '.env')
load_dotenv(dotenv_path)

def configLogging():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    if os.getenv('ENV') == 'production':
        logger.setLevel(logging.INFO)

configLogging()
