import psycopg2
import json
import pandas as pd
from sqlalchemy import create_engine

import data_handler


def load_config(filename='config.json'):
    try:
        with open(filename, 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        raise ValueError(f"구성 파일 '{filename}'을 찾을 수 없습니다.")


def postgres_con(config):
    user = config.get('db_user')
    password = config.get('db_password')
    host = config.get('db_host')
    port = config.get('db_port')
    db = config.get('db_name')

    if not (user and password and host and port and db):
        raise ValueError("DB 연결 정보를 찾을 수 없습니다. 환경 변수를 설정하세요.")

    pg_conn = psycopg2.connect(host=host, dbname=db, user=user, password=password, port=port)
    pg_cur = pg_conn.cursor()
    pg_engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")
    return pg_conn, pg_cur, pg_engine


def postgres_close(pg_conn, pg_cur):
    pg_conn.commit()
    pg_conn.close()
    pg_cur.close()


def create_table(conn, cur):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS Mydata (
        coordinates integer[],
        text_data text,
        numeric_data double precision
    );

    """
    cur.execute(create_table_sql)
    conn.commit()


def insert_data(conn, cur):
    data = data_handler.read_data(file_path='./data.json')

    # Mydata db의 (coordinates, text_data, numeric_data)칼럼에 값 넣기
    insert_data_sql = """
            INSERT INTO Mydata (coordinates, text_data, numeric_data)
            VALUES (%s, %s, %s);"""

    for item in data:
        cur.execute(insert_data_sql, (item['coordinates'], item['text_data'], item['numeric_data']))
    conn.commit()


def drop_table(name, cur):
    query = f"drop table if exists {name}"
    cur.execute(query)


def show_data(pg_engine):
    query = "select * from Mydata"
    pd.set_option('display.max_columns', None)
    df = pd.read_sql_query(query, pg_engine)
    print(df)
