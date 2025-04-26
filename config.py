import os

class Config:
    DEBUG = False
    TESTING = False
    REDIS_URL = os.environ.get('REDIS_URL', 'localhost')

class DevConfig(Config):
    DEBUG = True

class PrdConfig(Config):
    DEBUG = False