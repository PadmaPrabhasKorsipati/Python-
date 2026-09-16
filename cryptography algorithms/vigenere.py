p=input("Enter text:").upper()
k=input("Enter key:").upper()

e=""

for i in range(len(p)):

    if p[i].isalpha():
        e+=chr((ord(p[i])-65 + ord(k[i%len(k)])-65)%26 + 65)

    else:
        e+=i

print("Encrypted:"+e)

d=""

for i in range(len(e)):

    if e[i].isalpha():
        d+=chr((ord(e[i])-65 -(ord(k[i%len(k)])-65))%26 + 65)

    else:
        d+=i
print("Decrypted:"+d)