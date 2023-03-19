import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True
SECRET_KEY = os.environ.get('SECRET_KEY')
SESSION_EXPIRATE_MINUTES = 10
