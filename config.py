import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
SESSION_EXPIRATE_MINUTES = 10

APP_NAME = 'Flask API Target Data - CEP'

MONGODB_NAME = 'API_TARGET_DATA'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

