from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class TimeSeriesData(Base):
    __tablename__ = 'time_series_data'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    timestamp = Column(DateTime)
    value = Column(Float)

# Replace 'sqlite:///mydb.sqlite3' with the desired SQLite database file
engine = create_engine('sqlite:///mydb.sqlite3')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
