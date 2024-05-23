#!/bin/bash

CONTAINER_NAME="mysql-server"
MYSQL_ROOT_PASSWORD="my-secret-pw"
MYSQL_DATABASE="mydatabase"
MYSQL_USER="myuser"
MYSQL_PASSWORD="mypassword"
SQL_FILE_PATH="~/Cyber410fl/groupProject/init.sql"

docker pull mysql:latest

docker run --name $CONTAINER_NAME \
	-e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD \
	-e MYSQL_DATABASE=$MYSQL_DATABASE \
	-e MYSQL_USER=$MYSQL_USER \
	-e MYSQL_PASSWORD=$MYSQL_PASSWORD \
	-p 330:3306 \
	-d mysql:latest

echo "Waiting for MySQL to start..."
sleep 30

echo "Copying sql file" 
docker cp mydatabase.sql $CONTAINER_NAME:/

sleep 30

echo "Running docker exec"
docker exec -it $CONTAINER_NAME mysql -u root -p$MYSQL_ROOT_PASSWORD < /mydatabase.sql

