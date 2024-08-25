import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
DB_PORT = os.environ['DB_PORT']
MASTER_USER = os.environ['MASTER_USER']
MASTER_PASSWORD = os.environ['MASTER_PASSWORD']

engine = create_engine(
    f'postgresql://{MASTER_USER}:{MASTER_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}',
    pool_recycle=3600,
)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()