import psycopg2
import json
import pandas as pd
from sqlalchemy import create_engine
import data_handler


# config.json 파일에서 정보 불러오기
def load_config(filename='config.json'):
    try:
        with open(filename, 'r') as config_file:
            config = json.load(config_file)
        return config
    except FileNotFoundError:
        raise ValueError(f"구성 파일 '{filename}'을 찾을 수 없습니다.")


def postgres_con(config):   # config.json 에 저장된 db정보로 접속
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
    # 'Mydata' 이름의 테이블이 존재하지 않는다면 (coordinates, text_data, numeric_data) column을 갖는 테이블을 생성하는 쿼리
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
    query = f"drop table if exists {name}"  # 'name'의 테이블이 존재한다면 삭제시키는 쿼리
    cur.execute(query)



