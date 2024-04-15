# Encrypted data
encrypted_data_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# Convert encrypted data from hex to bytes
encrypted_data_bytes = bytes.fromhex(encrypted_data_hex)

# Flag format
flag_format = "crypto{"

# Iterate through all possible single-byte keys
for key in range(256):
    # Generate key repetition to match the length of the encrypted data
    repeated_key = bytes([key] * len(encrypted_data_bytes))
    
    # XOR the encrypted data with the repeated key
    decrypted_bytes = bytes([byte1 ^ byte2 for byte1, byte2 in zip(encrypted_data_bytes, repeated_key)])
    
    # Check if the decrypted data starts with the flag format
    if decrypted_bytes.startswith(flag_format.encode()):
        # Print the potential flag
        print("Potential flag:", decrypted_bytes.decode('utf-8'))
