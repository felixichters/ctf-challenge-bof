#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <time.h>

#define PASSWORD_FILE "/home/navi/Uni/it-sec/iap/presentation/race-condition/app/passwd"

int main() {
	int fd = open(PASSWORD_FILE, O_RDWR);

	if (fd < 0) {
		perror("open");
		return 1;
	}

	char buffer[33];
	srand(time(NULL));

	printf("Writing random hashes to %s...\n", PASSWORD_FILE);
	
	int j = 0;

	while (1) {
		for (int i = 0; i < 32; i++) {
			buffer[i] = "abcdef0123456789"[rand() % 16];
		}
		buffer[32] = '\0';
		usleep(5000);

		lseek(fd, 0, SEEK_SET);
		write(fd, buffer, strlen(buffer));
		j++;
		printf("%d\n", j);
		printf("updated hash ...\n", j);
    }
	close(fd);
	return 0;
}
