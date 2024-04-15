from pwn import xor
"""
a = key1
b = key2 ^ key1
=> key2= b^a
c = key2 ^ key3 
=> key3 = c^b^a
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

"""
def hex_byte(x):
    x=bytes.fromhex(x)
    return x
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
a = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
b = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
c = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
KEY1= hex_byte(KEY1)
a=hex_byte(a)
b=hex_byte(b)
c=hex_byte(c)
KEY2 = xor(a, KEY1)
KEY3 = xor(b,KEY2)
c = xor(c,KEY1)
c=xor(c,KEY2)
flag = xor(c,KEY3)
print(flag.decode('ascii'))

#