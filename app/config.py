import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://idoc:user_pwd@localhost/idoc_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
