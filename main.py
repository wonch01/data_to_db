import sample


def main():
    try:
        config = sample.load_config()
        conn, cur, engine = sample.postgres_con(config)
        sample.create_table(conn, cur)
        sample.insert_data(conn, cur)
        sample.show_data(engine)
        # sample.drop_table('sample_data', cur)

    except Exception as error:
        print("error:", error)
        return False
    finally:
        sample.postgres_close(conn, cur)

if __name__ == '__main__':
    main()