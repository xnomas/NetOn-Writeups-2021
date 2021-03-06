#!/usr/bin/python3
import os

"""
open the flag file, read, strip new lines and encode
"""
flag = open('flag.txt', 'r').read().strip().encode()

"""
generate a key of random 6 bytes
"""
key = os.urandom(6)
xored = b''

"""
iterate over the length of the flag 
and xor with the ith position modulo 6
"""
for i in range(len(flag)):
    xored += bytes([flag[i] ^ key[i % len(key)]])
print(f"Flag : {xored.hex()}")