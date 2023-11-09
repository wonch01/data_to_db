import sample

def main():
    try:
        conn, cur = sample.postgres_con('postgres', 1234, 'localhost',
                                         '5432', 'djtp_printer_monitoring_db')
        sample.create_table()
        sample.insert_data()
        sample.postgres_close(conn, cur)

    except Exception as error:
        print("error:", error)
        return False


if __name__ == '__main__':
    main()