import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'figure-frittuese-casking'
    SQLALCHEMY_DATABASE_URI = 'pymysql+mysql://localhost:3306/kindabyt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'pymysql+mysql://localhost:3306/kindabyt'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
