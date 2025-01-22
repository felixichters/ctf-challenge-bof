#include <stdio.h>
#include <string.h>

int main() {
    char buffer[256];
    char input[512];  // Allocate a larger buffer for potential overflow

    // Print the leaked address only once
    printf("Leaked: %p\n", (void *)buffer);
    fflush(stdout);  // Ensure the leak is printed immediately

    // Loop to continuously accept input and process payloads
    while (1) {
        
        // Read the payload from stdin
        if (fgets(input, sizeof(input), stdin) == NULL) {
            break;  // Exit the loop on EOF or error
        }

        // Remove the trailing newline character
        input[strcspn(input, "\n")] = '\0';

        // Copy the input to buffer using strcpy
        strcpy(buffer, input);

        // Print a response to stdout
        printf("Payload processed: %s\n", buffer);
        fflush(stdout);  // Ensure output is sent immediately
    }

    return 0;
}