import sys
sys.path.append('../')
from app import main_app as app

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql://{}:{}@{}/{}".format(app.config['DB_USER'], app.config['DB_PASSWD'],
                                                   app.config['DB_HOST'], app.config['DB_DATABASE']))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_database():
    from models import PriceRegistry
    Base.metadata.create_all(bind=engine)
