from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE = 'postgresql'
USER = 'postgres'
PASSWORD = 'password'
HOST = 'localhost'
PORT = '5431'
DB_NAME = 'test01'

CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

ENGINE = create_engine(
    CONNECT_STR
)
Base = declarative_base()