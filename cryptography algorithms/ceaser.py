c=input("Enter the text:").upper()
k=int(input("Enter key:"))

e=""

for i in c:
    if i.isalpha():
        e+=chr((ord(i)-65+k)%26+65)
    else:
        e+=i


print(f"Encrypted:"+e)

d=""

for i in e:
    if i.isalpha():
        d+=chr((ord(i)-65-k)%26+65)
    else:
        d+=i
print("Decrypted:"+d)
