FROM python:3.9

RUN pip install flask

RUN useradd -m ctf_user
USER ctf_user
WORKDIR /home/ctf_user

COPY challenge.c server.py exploit.py /home/ctf_user/
COPY password_file /home/ctf_user/password_file

RUN gcc -o challenge challenge.c -lpthread

EXPOSE 5000

CMD ./challenge & python server.py
