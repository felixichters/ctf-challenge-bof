FROM ubuntu:20.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    vim \
    && apt-get clean

RUN useradd -ms /bin/bash jeff
USER jeff

WORKDIR /home/jeff

COPY exploit.py /home/jeff/

RUN pip install requests
