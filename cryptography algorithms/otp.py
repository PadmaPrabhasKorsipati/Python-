p=input("Enter text:").upper()

k=list(map(int,input("Enter values").split()))

e=""

for i in range(len(p)):
    if p[i].isalpha():
     e+=chr((ord(p[i])-65 +k[i%len(k)])%26+65)

    else:
       e+=p[i]

print("Encrypted:"+e)

d=""
for i in range(len(e)):

   if e[i].isalpha():
      d+=chr((ord(e[i])-65-k[i%len(k)])%26+65)


   else:
      d+=e[i]

print("Decrypted:"+d)
      



