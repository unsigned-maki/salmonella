import os
from . import models
from mongoengine import *

DB_HOST = os.getenv("DB_HOST")

connect(host=DB_HOST)
