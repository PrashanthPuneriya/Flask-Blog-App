import os

DEBUG = True  # Turn this off in production mode ***
TESTING = False

SECRET_KEY = os.environ.get('SECRET_KEY')

DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
