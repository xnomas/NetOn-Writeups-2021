import string 


name = 'Charles Wheatstone'.upper()
ciphertext = 'QRRXDRPCKESRSNSWWY'

dedup = ''
for n in name:
	if n not in dedup:
		dedup += n

print(dedup)
