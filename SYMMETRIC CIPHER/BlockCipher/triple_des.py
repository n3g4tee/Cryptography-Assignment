import requests

weak_key = bytes.fromhex("01" * 8) + bytes.fromhex("fe" * 8)

r = requests.get("https://aes.cryptohack.org/triple_des/encrypt_flag/{}/".format(weak_key.hex()))
ciphertext = r.json()['ciphertext']

r = requests.get("https://aes.cryptohack.org/triple_des/encrypt/{0}/{1}/".format(weak_key.hex(), ciphertext))
flag = r.json()['ciphertext']
print(bytes.fromhex(flag))