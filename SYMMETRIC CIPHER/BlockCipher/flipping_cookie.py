import requests
from pwn import xor

def get_ciphertext():
    r = requests.get("http://aes.cryptohack.org/flipping_cookie/get_cookie")
    return r.json()['cookie']

def check_admin(cookie,iv):
    r = requests.get(f"http://aes.cryptohack.org/flipping_cookie/check_admin/{cookie}/{iv}")
    return r.json()

ciphertext = bytes.fromhex(get_ciphertext())
iv = ciphertext[:16]
cookie = ciphertext[16:].hex()

pt = b'admin=False;expiry='[:16]
pt_payload = b'admin=True;expiry='[:16]

#    ciphertext ^ iv = "admin=False"
# => ciphertext ^ iv ^ "admin=True" ^ "admin=False" = "admin=False" ^ "admin=True" ^ "admin=False"
# => ciphertext ^ (iv ^ "admin=True" ^ "admin=False") = "admin=True"
iv_payload = xor(pt_payload, pt, iv).hex()
print(check_admin(cookie, iv_payload)['flag'])