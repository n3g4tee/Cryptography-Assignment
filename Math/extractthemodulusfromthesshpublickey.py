from Crypto.PublicKey import RSA
f = open('C:\\Users\\DELL\\Python\\crypto\\bruce_rsa.pub', 'r')
pubkey = RSA.import_key(f.read())
print(pubkey.n)