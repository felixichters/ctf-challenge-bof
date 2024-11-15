from pwn import *

crash_address = 0x00007ffff7a99a9c 
offset = cyclic_find(crash_address)
print(f"Offset is {offset}")

#./a.out $(python3 -c 'from pwn import *; print(cyclic(200))')
