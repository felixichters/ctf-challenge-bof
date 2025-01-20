#include <stdio.h>
#include <string.h>

int main(int argc, char** argv) {
	char buffer[256];
  printf("Leaked: %p\n", buffer); 
	strcpy(buffer, argv[1]);
  //printf(strcpy(buffer, argv[1]));
  printf("%s\n", buffer); 
	
  return 0;
}