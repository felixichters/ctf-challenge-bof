#include <iostream>
#include <cstring>
#include <fstream>

void readKey(const char* path) {
	std::ifstream file(path);
	if (file.is_open()) {
    std::string line;
    while (getline(file, line)) {
        std::cout << line << std::endl;
    }
    file.close();
	}
}

void vulnerableFunction(const char* input) {
  char buffer[100]; 
  strcpy(buffer, input); 
  std::cout << "Processing data: " << buffer << std::endl;
}

int main(int argc, char *argv[]) {
  if (argc > 1) {
    vulnerableFunction(argv[1]);
  }
  return 0;
}
