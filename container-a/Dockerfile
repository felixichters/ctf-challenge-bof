FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
    openssh-client \
		build-essential \
    coreutils \
    bash \
    util-linux \
    && apt-get clean

RUN echo "ctf" > /root/flag.txt 
RUN chmod 400 /root/flag.txt

RUN useradd -m neo

USER neo
WORKDIR /home/neo

#COPY bof.asm /home/neo/bof.asm
#COPY susi.cpp /home/neo/susi.cpp
#RUN gcc -o /home/neo/susi /home/neo/susi.cpp 
#RUN chown root:root /home/neo/susi 
#RUN chmod u+s /home/neo/susi
CMD ["/bin/bash"]
