<<<<<<< HEAD
## Docker container for DB process
- PostgreSQL Docker Container
### how to run
- sudo docker-compose -f db_postres.yml up {-d}
=======
## Docker container set-up & run for DB process
- PostgreSQL Docker Container
### how to run
- sudo docker-compose -f db_postres.yml up {-d}
- screen -S {신규 스크린이름} # control + ad (스크린 나오기), screen -r (스크린으로 다시 들어가기)

### how to check status of container
- sudo docker network ls
- sudo docker inspect {container_name} | grep 172
<<<<<<< HEAD

### check using port
- sudo lsof -i :5432
- netstat -ntl | grep 5432

### postgresql connection
- sudo -i -u postgres
- psql -h localhost -p 5433 -U postgres -d postgres

### containers remove
- docker rm -f $(docker ps -aq)
- docker container prune -f

### images remove
- docker rmi -f $(docker images -q)

### postgresl address, port setting config 
- sudo vi /etc/postgresql/15/main/postgresql.conf 
  => listen_addresses="*"
  
- sudo vi /etc/postgresql/15/main/pg_hba.conf
  => IPv4 local connections:
     host	all	all	0.0.0.0/0	trust

### firewall port accept
- sudo ufw allow 5432/tcp

### postgresql restart
- systemctl restart postgresql

