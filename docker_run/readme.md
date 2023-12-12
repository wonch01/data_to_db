## Docker container set-up & run for DB process
- PostgreSQL Docker Container
### how to run
- sudo docker-compose -f db_postres.yml up {-d}
- screen -S {신규 스크린이름} # control + ad (스크린 나오기), screen -r (스크린으로 다시 들어가기)


### how to check status of container
- sudo docker network ls
- sudo docker inspect {container_name} | grep 172
