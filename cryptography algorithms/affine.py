p=input("Enter text:").upper()

a=int(input("Enter a coprime:"))

b=int(input("Enter a number from 0 to 25:"))

e=""

for i in p:

    if i.isalpha():
        e+=chr((a*(ord(i)-65) + b)%26 +65)

    else:
        e+=i

print("Encrypted:"+e)

d=""


for x in range(26):
    if(a*x)%26==1:
        inv=x
        break

for i in e:

    if i.isalpha():
        d+=chr((inv*((ord(i)-65)-b))%26+65)

    else:
        d+=i

print("Decrypted:"+d)




