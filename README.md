# data_to_db
# Python Postgresql 개발환경

- **언어:** Python 3.11
- **데이터베이스:** POSTGRES 15.5
- **Pip 버전:** Psycopg2 2.9.9
- **에디터:** PyCharm


- 패키지 다운로드 :
  pip install -r requirements.txt

  
- 실행하는 방법 :
  python3 main.py


- config 파일 구성하기 :

   config.json 파일에 id, password, host, port, name, schema 넣기


- 데이터 넣는 방법 : 

    sample.py - def insert_data()의 data에 데이터 넣기


- db에 연결하기 :

   config=sample.load_congig()로 정보 불러와  
conn, cur, engine = sample.postgres_con(config)로 연결

  
- table 만들기 :

   main.py - sample.create_table(conn,cur)로 테이블 생성


- 들어간 data 보기 :

   main.py - sample.show_data(engine) 으로 확인


- table 삭제하기 :

  main.py - sample.drop_table(name,cur)로 테이블 삭제


- TODO :

  docker - container 적용하기