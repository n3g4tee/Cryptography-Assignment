import requests, json, os
from Crypto.Cipher import AES

r = requests.get("https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/")
data = r.json()['ciphertext']
encrypted_flag = data[32:]

r = requests.get("https://aes.cryptohack.org/ecbcbcwtf/decrypt/{}/".format(encrypted_flag))
response = r.json()['plaintext']

data = bytes.fromhex(data)
response = bytes.fromhex(response)
flag = []
for i, v in enumerate(response):
    flag.append(chr(v ^ data[i]))

print(''.join(flag))


