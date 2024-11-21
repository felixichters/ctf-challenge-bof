FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y \
		&& apt-get install -y \
		openssh-client \
		nmap \
		gcc \
		gdb \
		python3 \
		nasm \
		neovim \
		g++ \
		cmatrix \
		coreutils \
		zsh \
		util-linux \
		&& apt-get clean

RUN sysctl -w kernel.randomize_va_space=0
RUN useradd -ms /bin/zsh neo

USER neo
RUN touch /home/neo/.zshrc
WORKDIR /home/neo

CMD ["zsh"]
