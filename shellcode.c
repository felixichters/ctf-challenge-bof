#include <unistd.h>

int main() {
    char *shell = "/bin/zsh";
    char *args[] = {shell, NULL};
    execve(shell, args, NULL);
    return 0;
}

