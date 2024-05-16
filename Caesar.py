def enc(txt):
  return "".join([chr((ord(i) - 65 + 3)%26 + 65) for i in txt])

def dec(txt):
  return "".join([chr((ord(i) - 65 - 3)%26 + 65) for i in txt])

text = input("Enter text:").upper()
print("Encrypted text:", enc(text))
print("Decrypted text:",dec(enc(text)))
