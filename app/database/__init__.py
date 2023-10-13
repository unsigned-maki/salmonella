import os
from . import models
from mongoengine import *

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")

connect(db=DB_NAME, username=DB_USER, password=DB_PASS, host=DB_HOST)
