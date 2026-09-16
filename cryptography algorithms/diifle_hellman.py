p=int(input("Prime p:"))
g=int(input("generator g:"))

a=int(input("Enter private key:"))

b=int(input("Ennter private key:"))


A=(g**a)%p

B=(g**b)%p

key1=(B**a)%p

key2=(A**b)%p

print("Alice public key:", A)
print("Bob public key:", B)
print("Alice shared key:", key1)
print("Bob shared key:", key2)