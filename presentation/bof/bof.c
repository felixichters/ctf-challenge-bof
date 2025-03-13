#include <stdio.h>

int main() {
	char buffer[256];
	printf("Leaked: %p\n", buffer);
	gets(buffer);
}
