from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2
from models import Base


engine = create_engine("postgresql+psycopg2://postgres:$@localhost:5432/tomato_counter")
Session = sessionmaker(bind=engine)

def recreate():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__=="__main__":
    recreate()