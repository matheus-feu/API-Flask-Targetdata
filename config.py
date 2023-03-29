import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.environ.get('SECRET_KEY')
SESSION_EXPIRATE_MINUTES = 10

MONGODB_SETTINGS = {
    'db': "API_TARGET_DATA",
    'host': os.environ.get('MONGODB_HOST'),
    'port': int(os.environ.get('MONGODB_PORT'))
}
