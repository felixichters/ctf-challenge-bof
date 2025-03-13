#include <stdio.h>
#include <stdlib.h>

char *gets(char *s);

void vuln() {
	char buffer[256];
	
	FILE *leak_file = fopen("leak.txt", "w");
	if (leak_file) {
		fprintf(leak_file, "Leaked: %p\n", buffer);
		fclose(leak_file);
	}
	
	printf("Access restricted, Provide your credentials: \n");
	gets(buffer);
}

int main() {
	printf("Init security systems...\n");
	printf("Warning: Legacy software detected. Upgrade recommended.\n");
	vuln();
	system("cmatrix");
	return 0;
}
