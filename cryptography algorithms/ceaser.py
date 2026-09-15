c=input("Enter Plain text:")
key=int(input("Enter key:"))
e=""
for i in c:
    if i.isalpha():
        e+=chr((ord(i.upper())-65 +key)%26 +65)
    else:
        e+=i

print(f"Encrypted text:{e}")

p=""
for i in e:
    if i.isalpha():
        p+=chr((ord(i)-65-key)%26 +65)

    else:
        p+=i

print(f"Decrypted text:{p}")
        