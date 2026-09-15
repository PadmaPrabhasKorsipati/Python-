p=input("Enter text:").upper()
k=input("Enter key:")

e=""

for i in p:
    if i.isalpha():
      e+=k[ord(i)-65]
    else:
       e+=i

print("Encrypted:"+e)


d=""

for i in e:
    if i.isalpha():
      d+=chr(k.index(i)+65)
    else:
       d+=i

print("Decrypted:"+d)


