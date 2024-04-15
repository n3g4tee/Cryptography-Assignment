import requests

URL = "https://aes.cryptohack.org/block_cipher_starter/"

r = requests.get(URL + "encrypt_flag")
encrypted_flag = r.json()['ciphertext']

r = requests.get(URL + "decrypt/" + encrypted_flag)
plaintext = r.json()['plaintext']
plaintext = bytes.fromhex(plaintext).decode()
print(plaintext)