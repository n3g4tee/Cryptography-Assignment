from Crypto.Cipher import AES
from pwn import xor
import requests


#   key = iv = d(c0) ^ p0

#   p0 = d(c0) ^ iv
#   p1 = d(c1) ^ c0 
#   p2 = d(c2) ^ c1

#   If c1=0, c0=c2 
#   ==> p0 ^ p2 = iv

text = "a" * 16
text = text.encode().hex()
r = requests.get("https://aes.cryptohack.org/lazy_cbc/encrypt/{}/".format(text))
ct = r.json()['ciphertext']

fake_ct = ct + "0" * 32 + ct
r = requests.get("https://aes.cryptohack.org/lazy_cbc/receive/{}/".format(fake_ct)) #r should be {"error": "Invalid plaintext: " + decrypted.hex()}
if "error" not in r.text:
    print("Request should be \"{\"error\": \"Invalid plaintext: \" + decrypted.hex()}")
else:
    data = r.json()['error'].replace("Invalid plaintext: ", "")
    p0 = bytes.fromhex(data[:32])
    p2 = bytes.fromhex(data[64:96])
    key = xor(p0, p2).hex()
    print("KEY: {}".format(key))
    r = requests.get("https://aes.cryptohack.org/lazy_cbc/get_flag/{}/".format(key))
    flag = bytes.fromhex(r.json()['plaintext'])
    print("FLAG: {}".format(flag))