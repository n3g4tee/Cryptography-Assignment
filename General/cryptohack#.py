from pwn import xor

text = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
x = bytes.fromhex(text)
# Known prefix and suffix
prefix = b'crypto{4}'
#myXORkey lv0 must 3E zz
key="myXORkey"
# Perform XOR operation between the ciphertext and prefix
result = xor(x, key)
# Print the result
print(result.decode('ascii'))
