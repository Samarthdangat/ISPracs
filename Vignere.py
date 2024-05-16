text = "RAMSWARUPK".upper()
key = "RANCHOBABA".upper()
print(f"Plain Text : {text}")
print(f"Key Text : {key}\n")

while(len(text) > len(key)):
    key += key

cipher = ""
for i in range(len(text)):
    cipher += chr(((ord(text[i]) - ord("A")) + (ord(key[i]) - ord("A")))%26 + ord("A"))
print(f"Cipher Text : {cipher}")

decipher = ""
for i in range(len(cipher)):
    decipher += chr(((ord(cipher[i]) - ord("A")) - (ord(key[i]) - ord("A")))%26 + ord("A"))
print(f"Decipher Text : {decipher}")
