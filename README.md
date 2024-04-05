#To pull image in docker
docker pull mysql:latest

#To create container 
docker run --name mysql_container -p 8001:3306 -e MYSQL_ROOT_PASSWORD=<your_password> -d mysql:latest

#Login to mysql
docker exec -it mysql_container mysql -uroot -p

#To create database
CREATE DATABASE mydatabase;

#To start the container
docker start container_id

#To see a list of all running containers
docker ps 

#To see all containers, including those that are stopped
docker ps -a

#There is a file called "createTables". If you run, it will create the required tables. 