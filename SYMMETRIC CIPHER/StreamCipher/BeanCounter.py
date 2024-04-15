import requests, os
from pwn import xor

# From the code below, we can see the same counter was used => Same 16 bytes keystream was used
# (self.stup is always False => Else: self.newIV = self.value - 0)

#class StepUpCounter(object):
#    def __init__(self, step_up=False):
#        self.value = os.urandom(16).hex()
#        self.step = 1
#        self.stup = step_up
#
#    def increment(self):
#        if self.stup:
#            self.newIV = hex(int(self.value, 16) + self.step)
#        else:
#            self.newIV = hex(int(self.value, 16) - self.stup)
#        self.value = self.newIV[2:len(self.newIV)]
#        return bytes.fromhex(self.value.zfill(32))
#
#    def __repr__(self):
#        self.increment()
#        return self.value

r = requests.get("https://aes.cryptohack.org/bean_counter/encrypt/")
ciphertext = bytes.fromhex(r.json()['encrypted'])
PNG_header = bytes.fromhex("89504E470D0A1A0A0000000D49484452")
keystream = xor(ciphertext[:16], PNG_header)
PNG_data = xor(ciphertext, keystream)

with open("bean-counter.png", 'wb') as f:
    f.write(PNG_data)

os.system(os.path.join(os.getcwd(), "bean-counter.png"))