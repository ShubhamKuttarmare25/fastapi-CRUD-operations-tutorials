from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


#replace @ --> %40  ||  default localhost -> 3306
URL_DATABASE = 'mysql+pymysql://root:Shubham%40123@localhost:3306/BlogApplication'

engine = create_engine(URL_DATABASE)


SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind= engine)

Base = declarative_base()

