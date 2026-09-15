p=input("Plain text:").upper()

a=int(input("a:"))

b=int(input("b:"))

e=""

for c in p:

    if c.isalpha():
        e+=chr((a*ord(c)-65 +b)%26 +65)

    else:
        e+=c

print("Encrypted:",e)

for x in range(26):

    if(a*x)%26==1:
        inv=x
        break

d=""
for c in e:

    if c.isalpha():
        d+=chr((inv*((ord(c)-65)-b))%26+65)

    else:
        d+=c

print("Decrypted:",d)

    




