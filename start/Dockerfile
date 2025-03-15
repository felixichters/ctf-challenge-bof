FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
		gcc \
		python3 \
		python3-pip \
		vim \
		openssh-server \
		zsh \
		ncurses-term \
		&& apt-get clean

RUN mkdir /var/run/sshd

RUN useradd -m user && echo 'user:0815' | chpasswd 
RUN echo 'PermitRootLogin no' >> /etc/ssh/sshd_config
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
EXPOSE 22

COPY exploit.sh /home/user/exploit.sh && chown user:user /home/user/exploit.sh
COPY symlink.c /home/user/symlink.c && chown user:user /home/user/symlink.c
RUN gcc symlink.c -o symlink

CMD ["/usr/sbin/sshd", "-D"]
