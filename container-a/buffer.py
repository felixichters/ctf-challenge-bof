from pwn import *

p = process('./vuln')

payload = cyclic(400)

p.sendline(payload)

p.wait()
core = p.corefile

offset = cyclic_find(core.read(core.sp, 4))
log.info(f"Offset to return address: {offset}")
