
from sqlalchemy import create_engine
import db.sql_queries as qu
from sqlalchemy import text
import pandas as pd




def create_connection_to_db():
    engine = create_engine(
        "postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}".format(
            db_username=qu.DATABASE['username'], 
            db_password=qu.DATABASE['password'],
            db_host=qu.DATABASE['host'],
            db_port=qu.DATABASE['port'],
            db_name=qu.DATABASE['name']
        ),
        echo=True
    )
    conn = engine.connect()
    conn.execute('commit')
    return conn

def create_database():
    engine = create_engine(
        "postgresql+psycopg2://{db_username}:{db_password}@{db_host}:{db_port}".format(
            db_username=qu.DATABASE['username'], 
            db_password=qu.DATABASE['password'],
            db_host=qu.DATABASE['host'],
            db_port=qu.DATABASE['port']
        ),
        echo=True
    )
    conn = engine.connect()
    conn.execute('commit')
    conn.execute(qu.CREATE)
    conn.execute(qu.GRANT)
    conn.execute('commit')
    conn.close()

def create_tables():
    conn = create_connection_to_db()
    with open("./db/tables.sql") as file:
        query = text(file.read())
        conn.execute(query)

def load_data(con):
    data = pd.read_csv('./data/demanda.csv')
    data.to_sql('demanda', con, if_exists='replace')

def prepare_everything():
    create_database()
    conn = create_connection_to_db()
    load_data(conn)
