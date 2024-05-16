def encrypt(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return ciphertext

plaintext = "OAK"
key = "SON"
encrypted_text = encrypt(plaintext, key)
print("Encrypted:", encrypted_text)
decrypted_text = encrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)
