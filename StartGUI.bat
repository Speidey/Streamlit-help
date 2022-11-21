@echo off

cd C:\Users\
docker build -t myapp1:latest .
docker run -d  -p 8501:8501 --name=testgui myapp1:latest