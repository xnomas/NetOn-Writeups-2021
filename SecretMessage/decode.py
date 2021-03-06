import string


message = 'Avpr wbo! lbh rnearq vg, gnxr lbhe njneq: ARGBA{a1p3_p0qr_zl_se13aq}'

lc = string.ascii_lowercase  
uc = string.ascii_uppercase

tcyph = str.translate(message, str.maketrans(lc[13:] + lc[:13] + uc[13:] + uc[:13],lc + uc))
print(tcyph)