#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>

int main(void) {
	const char *file = "./safe.txt";

	// time of check
	if (access(file, W_OK) != 0) {
		perror("access");
		exit(EXIT_FAILURE);
	}

	sleep(2);

	// time of use
	int fd = open(file, O_WRONLY | O_APPEND);
	if (fd < 0) {
		perror("open");
		exit(EXIT_FAILURE);
	}

	const char *msg = "Escalated privilege operation executed!\n";
	if (write(fd, msg, strlen(msg)) < 0) {
		perror("write");
		close(fd);
		exit(EXIT_FAILURE);
	}
	close(fd);

	return 0;
}

