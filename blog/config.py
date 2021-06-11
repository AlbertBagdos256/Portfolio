import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE')
    SECRET_KEY = 'h48gh423h0gh894hgh49gh2pg9u0923h84g'
    SQLALCHEMY_TRACK_MODIFICATIONS = False   
