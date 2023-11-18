import psycopg2
import json
import pandas as pd
from pandas import json_normalize
from sqlalchemy import create_engine
import db_handler


def read_data(file_path):
    with open(file_path, 'r', encoding='UTF8') as file:
        data = json.load(file)
    return data


def show_data(pg_engine):
    query = "select * from Mydata"
    pd.set_option('display.max_columns', None)
    df = pd.read_sql_query(query, pg_engine)
    print(df)


#결측치 row 값 삭제
def missing_data(pg_engine):
    query = "select * from Mydata"
    pd.set_option('display.max_columns', None)
    df = pd.read_sql_query(query, pg_engine)
    df = df.dropna(axis=0)
    return df




