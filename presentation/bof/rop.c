#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void win() {
	printf("Mach dich raus aus der Leitung!");
}

void vuln() {
	char buffer[64];
	gets(buffer);
}

int main() {
	vuln();
	return 0;
}
