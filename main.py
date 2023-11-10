import sample


def main():
    try:
        # sample.open_site()
        config = sample.load_config()
        conn, cur = sample.postgres_con(config)
        sample.create_table(conn,cur)
        sample.insert_data(conn,cur)
        sample.postgres_close(conn, cur)


    except Exception as error:
        print("error:", error)
        return False


if __name__ == '__main__':
    main()