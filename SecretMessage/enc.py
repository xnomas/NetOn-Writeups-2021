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