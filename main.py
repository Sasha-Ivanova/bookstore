import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker

from functions import filling_data, get_data
from models import create_tables


def main():
    os.environ['DRIVER'] = 'postgresql'
    os.environ['DB_HOST'] = 'localhost'
    os.environ['DB_PORT'] = '5432'
    driver = os.getenv('DRIVER')
    login = 'postgres'
    password = '23112019'
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT')
    name_db = 'netology_db'
    DSN = f'{driver}://{login}:{password}@{host}:{port}/{name_db}'
    engine = sqlalchemy.create_engine(DSN)
    create_tables(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    filling_data(session)
    get_data(session)


if __name__ == "__main__":
    main()
