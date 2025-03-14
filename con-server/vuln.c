
#include <stdio.h>
#include <unistd.h>
#include <string.h>

#define DELAY 500000

int main(int argc, char * argv[]) { 
	char * fileName = argv[1];
	char buffer[420];
	
	strncpy(buffer, argv[2], sizeof(buffer) - 1);
	buffer[sizeof(buffer) - 1] = '\0'; // Ensure null-termination
	
	int i;
	FILE * fileHandler;

	if(!access(fileName, W_OK)) {
		for(i = 0; i < DELAY;i++) {
			int a = i ^ 2;
		}

		fileHandler = fopen(fileName, "a+"); 
		fwrite(buffer, sizeof(char), strlen(buffer), fileHandler); 
		fclose(fileHandler);
	} else {
		printf("No permission n");
	}
}
