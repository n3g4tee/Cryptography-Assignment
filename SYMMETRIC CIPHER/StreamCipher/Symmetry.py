import requests

BASE_URL = "https://aes.cryptohack.org/symmetry/"

r = requests.get(BASE_URL + "encrypt_flag/")
data = r.json()['ciphertext']
encrypted_flag = data[32:]
iv = data[:32]

r = requests.get(BASE_URL + "encrypt/{0}/{1}/".format(encrypted_flag, iv))
flag = bytes.fromhex(r.json()['ciphertext'])
print(flag)