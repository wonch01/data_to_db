# data_to_db
# Python Postgresql 개발환경

- **언어:** Python 3.11
- **데이터베이스:** POSTGRES 15.5
- **Pip 버전:** Psycopg2 2.9.9
- **에디터:** PyCharm


- config 파일 구성하기 :

   config.json 파일에 id, password, host, port, name, schema 넣기


- 데이터 넣는 방법 : 

    def insert_data()의 data에 데이터 넣기


- db에 연결하기 :

   config=sample.load_congig()로 정보 불러와  
conn, cur, engine = sample.postgres_con(config)로 연결

  
- table 만들기 :

   sample.create_table(conn,cur)로 테이블 생성


- 들어간 data 보기 :

   sample.show_data(engine) 으로 확인
