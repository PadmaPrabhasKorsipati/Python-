p=input("Enter the text:").upper()
key=input("Enter the key:").upper()


s=""

for c in key+"ABCDEFGHIJKLMNOPQRSTUVWXYZ":
     if c not in s:
          s+=c

print("cipher alphabet",s)

e=""
for c in p:

  e+=s[ord(c)-65] if c.isalpha() else c

print("Encrypted",e)



     