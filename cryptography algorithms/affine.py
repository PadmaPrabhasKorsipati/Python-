p=input("Enter the text:").upper()
a=int(input("Enter a:"))
b=int(input("Enter b:"))

r=""

for c in p:
    if c.isalpha():
        r+=chr((a*ord(c)-65+b)%26 +65)

    else:
        r+=c

print("Encrypted",r)

