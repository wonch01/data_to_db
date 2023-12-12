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
    query = "select * from mydata"      # mydata 의 모든 값을 가져오는 쿼리
    pd.set_option('display.max_columns', None)  # df의 모든 column을 보이게 해줌
    df = pd.read_sql_query(query, pg_engine)
    print(df)


# data to json
def data_to_json(pg_engine):
    query = "select * from mydata"      # mydata 의 모든 값을 가져오는 쿼리
    df = pd.read_sql_query(query, pg_engine)
    df_json = df.to_json()
    return df_json


def select_data(engine, query):
    # select query example)
    # select numeric_data from mydata where numeric_data > 0.5
    # -> Mydata 테이블에서 numeric_data 값이 0.5 이상인 값들을 가져오는 쿼리
    df = pd.read_sql_query(query, engine)
    print("select_data :", df)
    return df


# 결측치 row 값 삭제
def missing_data(pg_engine):
    query = "select * from mydata"      # mydata 의 모든 값을 가져오는 쿼리
    df = pd.read_sql_query(query, pg_engine)
    df = df.dropna(axis=0)              # axis=1은 결측치 열이 제거
    return df


#data 중복값 삭제
def drop_duplicates(pg_engine):
    query = "select * from mydata"
    pd.set_option('display.max_columns', None)
    df = pd.read_sql_query(query, pg_engine)
    df.drop_duplicates(subset='text_data')
    return df


