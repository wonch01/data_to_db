## Docker container for DB process
- PostgreSQL Docker Container
### how to run
- sudo docker-compose -f db_postres.yml up {-d}

### how to check status of container
- sudo docker network ls
- sudo docker inspect {container_name} | grep 172
