FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
		gcc \
		gdb \
		python3 \
		python3-pip \
		vim \
		openssh-server \
		zsh \
		&& apt-get clean

RUN pip install pwntools

RUN useradd -m user && echo 'user:0815' | chpasswd

RUN chsh -s /usr/bin/zsh user

RUN mkdir /var/run/sshd
RUN echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
EXPOSE 22

COPY vuln.c /home/user/vuln.c
COPY exploit.py /home/user/exploit.py
RUN gcc -fno-stack-protector -z execstack home/user/vuln.c -o /home/user/vuln

RUN chown user:user /home/user
RUN chown root:root /home/user/vuln
RUN chmod +s /home/user/vuln

CMD ["/usr/sbin/sshd", "-D"]
