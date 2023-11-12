import psycopg2
import json
import pandas as pd
from sqlalchemy import create_engine


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


def create_table(conn,cur):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS sample_data (
        coordinates integer[],
        text_data text,
        numeric_data double precision
    );
    
    """
    cur.execute(create_table_sql)
    conn.commit()


def insert_data(conn,cur):
    data = [
        (   [[24, 8], [110, 8], [110, 16], [24, 16]],
            '미로나스국T리! 괴갑대쏘다',
            0.0017230819330160733),
        (   [[10, 16], [56, 16], [56, 24], [10, 24]],
            '(P못 피스a(끼기',
            0.006269590404310938),
        ([[91, 73], [143, 73], [143, 89], [91, 89]], '사갑럽니다', 0.1783492257449009),
        (   [[91, 91], [223, 91], [223, 105], [91, 105]],
            '바람이념신물더러온 그순간부터 ',
            0.10488713129482491),
        (   [[170, 290], [200, 290], [200, 296], [170, 296]],
            '거파y3 너',
            0.017439958583245804),
        (   [[99, 297], [167, 297], [167, 311], [99, 311]],
            '미아지키하아오',
            0.6818672154523849),
        (   [[43, 313], [251, 313], [251, 375], [43, 375]],
            '바람이 붙다',
            0.6794710701367007),
        (   [[65, 391], [223, 391], [223, 405], [65, 405]],
            '9리s임 가슴-속데간되다 그리움음 만니세인',
            0.012198750988838075)
        ]

    insert_data_sql = """
            INSERT INTO sample_data (coordinates, text_data, numeric_data)
            VALUES (%s, %s, %s);"""

    for item in data:
        cur.execute(insert_data_sql, (item[0], item[1], item[2]))
    conn.commit()


def drop_table(name, cur):
    query = f"drop table if exists {name}"
    cur.execute(query)


def show_data(pg_engine):
    query = "select * from sample_data"
    pd.set_option('display.max_columns', None)
    df = pd.read_sql_query(query, pg_engine)
    print(df)

