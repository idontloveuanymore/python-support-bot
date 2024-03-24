import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
START_MESSAGE = os.getenv('START_MESSAGE')