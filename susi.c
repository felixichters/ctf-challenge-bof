#include <stdio.h>
#include <string.h>
void vulnerable_function() {
	char buffer[64];
  printf("Buffer is located at: %p\n", buffer); 
  printf("Red pill or blue pill ? ");
  gets(buffer);
}

int main(int argc, char** argv) {
	char buffer[256];
  printf("Buffer is located at: %p\n", buffer); 
	strcpy(buffer, argv[1]);
  return 0;
}

