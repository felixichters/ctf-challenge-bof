FROM python:3.9

WORKDIR /app

COPY server.py vuln.c /app/

RUN pip install flask
RUN apt-get install -y gcc

RUN gcc vuln.c -o vuln
RUN chown root:root vuln
RUN chmod +s vuln

EXPOSE 5000

CMD ["python", "server.py"]
