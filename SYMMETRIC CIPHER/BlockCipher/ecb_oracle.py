from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests, string, time

def get_request(text):
    print(text)
    plaintext = text.encode().hex()
    r = requests.get("https://aes.cryptohack.org/ecb_oracle/encrypt/{}/".format(plaintext))
    time.sleep(0.2)
    return r

#Guess the length of the FLAG ==> len(FLAG) <= 32 ==> using 2 blocks
def guess_the_length():
    text = "a"
    r = get_request(text.encode().hex())
    data = r.json()['ciphertext']
    print(len(bytes.fromhex(data)))

def attack():
    #First part of a FLAG: crypto{ 
    flag = ""
    guess_data = string.ascii_lowercase + string.ascii_uppercase + string.digits + '{' + '_'+'@'+'}'
    block1 = []
    block2 = []

    #Get the encrypted block
    for i in range(16 - 1):
        text = "a" * (16 - i - 1)
        r = get_request(text)
        print(r.text)
        block1.append(r.json()['ciphertext'][:32])
        block2.append(r.json()['ciphertext'][32:64])
    
    #The web don't accept get request with null string, so i do some exception here, not having time to fix this =((
    r = get_request("a" * 16)
    block1.append(r.json()['ciphertext'][32:64])
    block2.append(r.json()['ciphertext'][64:96])

    #Guess the characters
    for i in range(32):
        for j in guess_data:
            if len(flag) < 16:
                guess = "a" * (16 - len(flag) - 1) + flag + j
                r = get_request(guess)
                tmp_res = r.json()['ciphertext'][:32]
                if (tmp_res == block1[len(flag)]):
                    flag += j
                    print(flag)
                    break
            
            else: 
                k = i % 16
                guess = flag[k+1:] + j 
                r = get_request(guess)
                tmp_res = r.json()['ciphertext'][:32]
                if (tmp_res == block2[k]):
                    flag += j
                    print(flag)
                    break
            if flag[-1] == '}':
                return

if __name__ == "__main__":
    attack()
