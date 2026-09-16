p=input("Enter text:").upper()
k=input("Enter key:").upper()

e=""

for i in range(len(p)):

    if i.isalpha():
        e+=chr((ord(k[i])-65 + ord(k[i%len(k)])-65)%26 + 65)

    else:
        e+=i

print("Encrypted:"+e)

d=""

for i in range(len(e)):

    if i.isalpha():
        d+=chr((ord(k[i])-65 -(ord(k[i%len(k)])-65))%26 + 65)

    else:
        d+=i
print("Decrypted:"+d)