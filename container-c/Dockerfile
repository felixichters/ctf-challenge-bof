FROM python:3.9

WORKDIR /app

COPY server.py .
COPY dirty.c .
COPY passwd /app/passwd

RUN pip install flask

RUN gcc -o dirty dirty.c

EXPOSE 5000

CMD ["bash", "-c", "./dirty & python server.py"]
