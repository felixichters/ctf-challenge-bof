FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get upgrade -y 
RUN apt-get install -y gcc g++ python3 sudo vim gdb 
RUN apt-get clean

RUN echo 0 | tee /proc/sys/kernel/randomize_va_space

RUN echo "ssh oder so" > /root/flag.txt 
RUN chmod 400 /root/flag.txt

RUN useradd -ms /bin/bash neo

USER neo
WORKDIR /home/neo

COPY bof.asm /home/neo/bof.asm
COPY susi.cpp /home/neo/susi.cpp
RUN gcc -o /home/neo/susi /home/neo/susi.cpp 
RUN chown root:root /home/neo/susi 
RUN chmod u+s /home/neo/susi

CMD ["/bin/bash"]
