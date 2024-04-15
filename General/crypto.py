import base64
ords = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
print("Here is your flag:")
text = bytes.fromhex(ords)
print(text)
encoded_text = base64.b64encode(text)
print(encoded_text)