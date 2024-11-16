FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y \
    vim \
    gcc \
		gdb \
		python3 \
		nasm \
    build-essential \
    coreutils \
    bash \
    util-linux \
    && apt-get clean

RUN sysctl -w kernel.randomize_va_space=0

RUN echo "ctf" > /root/flag.txt 
RUN chmod 400 /root/flag.txt

RUN useradd -m smith

USER smith
WORKDIR /home/smith

COPY bof.asm /home/smith/bof.asm
COPY susi.cpp /home/smith/susi.cpp
RUN gcc -o /home/smith/susi /home/smith/susi.cpp 
#RUN chown root:root /home/smith/susi 
#RUN chmod u+s /home/smith/susi
CMD ["/bin/bash"]
