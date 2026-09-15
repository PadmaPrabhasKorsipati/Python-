c=input("Enter text:").upper()
k=input("Enter text:")

e=""

for i in c:

    if i.isalpha():
        e+=k[ord(i)-65]

    else:
        e+=i

print(f"Encrypted text:{e}")


p=""

for i in e:

    if i.isalpha():
        p+=chr(k.index(i)+65)

    else:
        p+=i

print(f"Decrypted text:{p}")