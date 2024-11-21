section .data
	shell db '/bin/sh', 0

section .text
    global _start

_start:
    mov rax, 59             
    mov rdi, shell          
    xor rsi, rsi            
    xor rdx, rdx            
  
    syscall                 
    
		mov rax, 60            
    xor rdi, rdi          
    syscall                 
