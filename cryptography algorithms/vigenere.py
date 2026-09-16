p=input("Enter text:")
k=input("Enter key:")

e=""

for i in p:

    if i.isalpha():
        e+=chr((ord(i)-65 + ord(k[i%len(k)])-65)%26 + 65)

    else:
        e+=i

print("Encrypted:"+e)

d=""

for i in e:

    if i.isalpha():
        d+=chr((ord(i)-65 -(ord(k[i%len(k)])-65))%26 + 65)

    else:
        d+=i
print("Decrypted:"+d)