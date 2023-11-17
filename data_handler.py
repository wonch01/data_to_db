import psycopg2
import json
import pandas as pd
from sqlalchemy import create_engine
import db_handler


def read_data(file_path):
    with open(file_path, 'r', encoding='UTF8') as file:
        data = json.load(file)
    return data


def select_data(query):
    insert_query = query
    config = sample.load_config()
    conn, cur, engine = sample.postgres_con(config)
    df = pd.read_sql_query(insert_query, engine)
    return df






