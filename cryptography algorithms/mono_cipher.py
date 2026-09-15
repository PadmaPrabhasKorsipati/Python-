p=input("Enter text")
key=input("Enter key:").upper()

def encrypt(s):
    r=""

    for c in s:

        r+=key[ord(c)-65] if c.isalpha() else c

    return r


e = encrypt(p.upper())
print("Encrypted:", e)