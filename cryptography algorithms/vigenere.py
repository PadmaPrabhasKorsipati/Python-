p=input("Enter the plain text:").upper()

key=input("Enter the key text:").upper();


e=""

for i in range(len(p)):


    if p[i].isalpha():
        e+=chr((ord(p[i])-65 + ord(key[i%len(key)])-65)%26 +65)

    else:
        e+=p[i]


print(f"Encrypted text:{e}")


c=""

for i in range(len(p)):

    if e[i].isalpha():
        c+=chr((ord(e[i]-65 -ord(key[i%len(key)])-65))%26 +65)

    else:
        c+=e[i]

print(f"Decrypted text:{c}")