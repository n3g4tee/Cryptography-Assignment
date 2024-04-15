from Crypto.Util.number import *
ords=11515195063862318899931685488813747395775516287289682636499965282714637259206269
enc=hex(ords)[2:]
enc1=bytes.fromhex(enc)
enc2=enc1.decode('ascii')
print(enc2)