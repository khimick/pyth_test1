FROM python:3.7.7-alpine
workdir /app
COPY . .
CMD ["/usr/local/bin/python3", "/app/app.py"]  