import os

from dotenv import load_dotenv

load_dotenv()

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
SESSION_EXPIRATE_MINUTES = 10

APP_NAME = 'Flask API Target Data - CEP'

MONGODB_SETTINGS = {
    'db': "API_TARGET_DATA",
    'host': os.environ.get('MONGODB_HOST', 'localhost'),
    'port': int(os.environ.get('MONGODB_PORT', '27017'))
}

