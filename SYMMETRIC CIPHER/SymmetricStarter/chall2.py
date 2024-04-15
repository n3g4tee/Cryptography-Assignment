import hashlib, requests, json
from Crypto.Cipher import AES

r = requests.get("https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words")
lst = r.text.splitlines()

r =  requests.get("https://aes.cryptohack.org/passwords_as_keys/encrypt_flag/")
encrypted_flag = r.json()['ciphertext']

def decrypt(KEY, ciphertext):
    cipher = AES.new(KEY, mode=AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

for i in lst:
    key = hashlib.md5(i.encode()).digest()
    encrypted = bytes.fromhex(encrypted_flag)
    plaintext = decrypt(key, encrypted)
    if b'crypto' in plaintext:
        print(f'FOUND: {plaintext}')




