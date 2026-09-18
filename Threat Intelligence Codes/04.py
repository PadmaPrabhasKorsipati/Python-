p = input("Enter message: ")
key = input("Enter key: ")

e = ""
for i in range(len(p)):
    e += chr(ord(p[i]) ^ ord(key[i % len(key)]))

print("Encrypted:", e)

d = ""
for i in range(len(e)):
    d += chr(ord(e[i]) ^ ord(key[i % len(key)]))

print("Decrypted:", d)