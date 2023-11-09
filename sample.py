import psycopg2


def postgres_con(user, password, host, port, db):
    pg_conn = psycopg2.connect(host=host, dbname=db, user=user, password=password, port=port)
    pg_cur = pg_conn.cursor()
    # pg_engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")
    return pg_conn, pg_cur


def postgres_close(pg_conn, pg_cur):
    pg_conn.commit()
    pg_conn.close()
    pg_cur.close()


def create_table(conn,cur):
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS table_name (
        id serial ,
        coordinates integer[],
        text_data text,
        numeric_data double precision,
        binary_image bytea
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
            INSERT INTO table_name (coordinates, text_data, numeric_data)
            VALUES (%s, %s, %s);"""

    for item in data:
        cur.execute(insert_data_sql, (item[0], item[1], item[2]))
    conn.commit()

