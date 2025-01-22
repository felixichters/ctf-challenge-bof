#include <stdio.h>
#include <string.h>

int main() {
    char buffer[16];

    printf("Leaked address: %p\n", (void*)buffer);

    printf("Enter your input: ");
    fflush(stdout); 

    char input[512];
    fgets(input, sizeof(input), stdin);

    strcpy(buffer, input);

    printf("You entered: %s\n", buffer);
    
	return 0;
}

