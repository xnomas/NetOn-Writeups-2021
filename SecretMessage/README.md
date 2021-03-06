# Secret Message

Author: X4v1l0k
```
Write your own decoder
```

## Encoder

In this challenge we have some source code `enc.py` and the flag in an encoded format in `flag.txt`:
```py
def encrypt(pwd, s):
	n = 0
	for c in pwd: n += ord(c)
	lc = string.ascii_lowercase  
	uc = string.ascii_uppercase	
	tcyph = str.translate(s, str.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13]))
	fcyph = ''
	for c in tcyph: fcyph += chr(ord(c) + n)
	return fcyph
```
^ That is the encoding function, but I decided to pretty it up a bit:
```py
def encrypt(pwd, s):
	n = 0
	for c in pwd: 
		n += ord(c) # get ascii value of c, add to n

	"""
	lc + uc = all letters upper and lower
	"""
	lc = string.ascii_lowercase  
	uc = string.ascii_uppercase
	
	"""
	>>> lc[13:]+lc[:13]
'		nopqrstuvwxyzabcdefghijklm
	>>> uc[13:]+uc[:13]
		NOPQRSTUVWXYZABCDEFGHIJKLM
	"""

	tcyph = str.translate(s, str.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13]))
	fcyph = ''
	
	for c in tcyph: 
		fcyph += chr(ord(c) + n)
	
	"""
	fcyph is 68 characters
	"""

	return fcyph
```
I had to do some research on `str.translate()` and `str.maketrans()`. `.translate()` translates an alphabet based on mappings by `.maketrans()`. `.maketrans()` Takes the original alphabet as its first argument, in this case its the lowercase + uppercase ascii letters. Then the slices split the alphabet in half and switch them:
```python
lc[13:]+lc[:13] == 'nopqrstuvwxyzabcdefghijklm'
uc[13:]+uc[:13] == 'NOPQRSTUVWXYZABCDEFGHIJKLM'
```
So putting this against the original alphabet:
```
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ <- before translation
nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM <- after translation
```
So for example `NETON` translates to `ARGBA`. Nice! 

## Finding the offset

From `encode.py` we know that the encoding is not just a translation, but an offset `n` is added to the ascii values of each character of the final message. `n` is the sum of ascii values of some password `pwd`. Since we don't have that, there is an option to bruteforce:
```py
import string



lc = string.ascii_lowercase  
uc = string.ascii_uppercase

tcyph = str.translate('NETON', str.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13]))
fcyph = ''

neton = '̜͍͑͋˻͒̽͊˼˻͇̽̓˻͍͉̼͍̀͌˻͑͂̇˻͉͓͍͂˻͇̽̓̀˻͉͉̀͌̕ͅ˻̢̜̭̝̜͖̼̺͍̺͕͇̺͎̼̌͋̎͋̋͌̀̌̎͌͘'



for n in range(200,1000):
	for c in neton:
		fcyph = fcyph + chr(ord(c) - n)
	print(f'n: {n} result: {fcyph}')
	fcyph = ''
```
I was just iterating through an arbitrary range of offsets that made sense to me, it would have to be a pretty large one! From there, I found some great output:
```

n: 731 result: Avpr wbo! lbh rnearq vg, gnxr lbhe njneq: ARGBA{a1p3_p0qr_zl_se13aq}

```
Now remember: `NETON = ARGBA`. So we have the flag! Now just to decode:
```py
import string


message = 'Avpr wbo! lbh rnearq vg, gnxr lbhe njneq: ARGBA{a1p3_p0qr_zl_se13aq}'

lc = string.ascii_lowercase  
uc = string.ascii_uppercase

tcyph = str.translate(message, str.maketrans(lc[13:] + lc[:13] + uc[13:] + uc[:13],lc + uc))
print(tcyph)
```
Output: 
```
Nice job! you earned it, take your award: NETON{n1c3_c0de_my_fr13nd}
```
A very nice challenge indeed.