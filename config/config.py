import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

DATABASE_NAME: str = os.getenv('DATABASE_NAME')
DATABASE_USER: str = os.getenv('DATABASE_USER')
DATABASE_PASSWORD: str = os.getenv('DATABASE_PASSWORD')
DATABASE_HOST: str = os.getenv('DATABASE_HOST')
DATABASE_PORT: str = os.getenv('DATABASE_PORT')
