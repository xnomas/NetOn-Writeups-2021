import os
import binascii

flag = binascii.unhexlify(b'5bbed19a19234dcbf78a3e0b4abcb5e5330721a4b5a3322a7397b5a22a')

key = b'\x15\xfb\x85\xd5WX'

xored = ''

for i in range(len(flag)):
	xored += chr(flag[i] ^ key[i % 6])
print(f"Flag : {xored}")