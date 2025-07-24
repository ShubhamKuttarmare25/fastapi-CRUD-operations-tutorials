from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#Always URL-encode special characters in the password portion of a PostgreSQL URI string.
# Character	URL Encoded
# @	%40
# :	%3A
# /	%2F
#	%23
#URL_DATABASE = 'postgresql://postgres:Shubham@8329@localhost:5432/QuizApplication'
URL_DATABASE = 'postgresql://postgres:Shubham%408329@localhost:5432/QuizApplication'



engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()







