import string



lc = string.ascii_lowercase  
uc = string.ascii_uppercase

tcyph = str.translate('NETON', str.maketrans(lc + uc, lc[13:] + lc[:13] + uc[13:] + uc[:13]))
fcyph = ''

neton = '̜͍͑͋˻͒̽͊˼˻͇̽̓˻͍͉̼͍̀͌˻͑͂̇˻͉͓͍͂˻͇̽̓̀˻͉͉̀͌̕ͅ˻̢̜̭̝̜͖̼̺͍̺͕͇̺͎̼̌͋̎͋̋͌̀̌̎͌͘'



for n in range(724,750):
	for c in neton:
		fcyph = fcyph + chr(ord(c) - n)
	print(f'n: {n} result: {fcyph}')
	fcyph = ''

"""
n: 731 result: Avpr wbo! lbh rnearq vg, gnxr lbhe njneq: ARGBA{a1p3_p0qr_zl_se13aq}
"""
