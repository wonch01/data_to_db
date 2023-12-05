import db_handler
import data_handler


def main():
    try:
        config = db_handler.load_config()
        conn, cur, engine = db_handler.postgres_con(config)
        # db_handler.create_table(conn, cur)
        # db_handler.insert_data(conn, cur)
        data_handler.show_data(engine)
        db_handler.select_data(engine, 'select numeric_data from Mydata where numeric_data > 0.5')
        # data_handler.missing_data(engine)
        # sample.drop_table('Mydata', cur)

    except Exception as error:
        print("error:", error)
        return False
    finally:
        db_handler.postgres_close(conn, cur)


if __name__ == '__main__':
    main()
