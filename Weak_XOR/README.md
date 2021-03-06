# Weak XOR

Author: N0xi0us
```
Will you be able to break the cipher and obtain the flag?
```

## encrypt.py

The source code responsible for 'encryption' is available to us in `encrypt.py`:
```py
#!/usr/bin/python3
import os
flag = open('flag.txt', 'r').read().strip().encode()
key = os.urandom(6)
xored = b''
for i in range(len(flag)):
    xored += bytes([flag[i] ^ key[i % len(key)]])
print(f"Flag : {xored.hex()}")
```
And the xored flag is `5bbed19a19234dcbf78a3e0b4abcb5e5330721a4b5a3322a7397b5a22a`. So I decided to pretty up the code a bit:
```py
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
```
Cool. So how can we recover the key and with it the flag? Well, XOR is an unsafe operation. Its inverse is itself. And we know the first six letters `NETON{` which is also the length of the key! Since it is bytes, that gives us 256 options for each position. Time to script that:

## brute.py

I did this in a very heavy handed way:
```py
import os
import binascii

flag = binascii.unhexlify(b'5bbed19a19234dcbf78a3e0b4abcb5e5330721a4b5a3322a7397b5a22a')

keys = []
for i in range(2000): # to make sure we generate all 256 bytes
	temp = os.urandom(1)
	if temp not in keys:
		keys.append(temp)

for i in keys:
	xored = ''
	xored += chr(flag[5] ^ int.from_bytes(key,byteorder='big'))
	if xored == '{':
		print(f"Flag : {xored} Key 1 : {key}")
```
And then I just changed the for loop for each letter from `NETON{` and got the following key: `key = b'\x15\xfb\x85\xd5WX'`</br>
So to get the flag:
```py
import os
import binascii

flag = binascii.unhexlify(b'5bbed19a19234dcbf78a3e0b4abcb5e5330721a4b5a3322a7397b5a22a')

key = b'\x15\xfb\x85\xd5WX'

xored = ''

for i in range(len(flag)):
	xored += chr(flag[i] ^ key[i % 6])
print(f"Flag : {xored}")
```
And the flag is: `NETON{X0r_iS_G00d_4_0verfl0w}`