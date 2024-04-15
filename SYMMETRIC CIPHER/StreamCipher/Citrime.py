import requests
import string

alphabet = string.ascii_letters + string.digits + "}" + "_" + "!" + "?" + "@"

def get_request(plaintext):
    text = plaintext.encode().hex()
    r = requests.get("https://aes.cryptohack.org/ctrime/encrypt/{}/".format(text))
    return r.json()['ciphertext']

flag = "crypto{"
length = len(get_request(flag))

while (not flag.endswith("}")):
    for i in alphabet:
        print(i)
        tmp = get_request(flag + i)
        if len(tmp) == length:
            flag = flag + i
            print(flag)
            break


 