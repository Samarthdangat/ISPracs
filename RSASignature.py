import hashlib

p = int(input("Enter P : "))
q = int(input("Enter Q : "))

n = p*q
phi = (p - 1)*(q - 1)

def encrypt(key, plaintext):
    d, n = key
    cipher = plaintext**d % n
    return cipher

def decrypt(key, ciphertext):
    e, n = key
    decipher = ciphertext**e % n
    return decipher

message = "Hello"
message_hash = int(hashlib.md5(message.encode()).hexdigest(), 16) % n
print(f"\nMessage : {message}")
print(f"Message Digest : {message_hash}")

e = 2
while math.gcd(e , phi) != 1:
   e += 1
d = pow(e,-1,phi)

print(f"\nPublic Key : {(e, n)}")
print(f"Private Key : {(d, n)}")

signature = encrypt((d, n), message_hash)
print(f"\nSignature : {signature}")
print(f"Sender Send (Message, Signature) to Receiver : {(message, signature)}")

message_hash = int(hashlib.md5(message.encode()).hexdigest(), 16) % n
print(f"\nHash of message at Receiver : {message_hash}")

hashfromsignature = decrypt((e, n), signature)
print(f"Hash from signature : {hashfromsignature}")

if hashfromsignature == message_hash:
    print("\nVerifed as both hash matches")
else:
    print("\nError")
