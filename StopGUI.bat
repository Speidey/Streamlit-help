@echo off

docker stop testgui
docker rm testgui
docker rmi myapp1:latest