p=input("Enter text: ").upper()
key=input("Enter key: ").upper()

r=""
j=0
for c in p:
    if c.isalpha():
        r+=chr((ord(c)-65+ord(key[j%len(key)])-65)%26+65)
        j+=1

    else:
        r+=c
print("Encrypted:",r)

