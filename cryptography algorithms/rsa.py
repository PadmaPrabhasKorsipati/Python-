p=int(input("Enter p:"))

q=int(input("Enter q:"))

e=int(input("Enter e:"))

m=int(input("Enter message:"))


n=p*q

phi=(p-1)*(q*1)

for d in range(1,phi):
    if(e*d)%phi==1:
        break

c=(m**e)%n

print("Encrypted:",c)


x=(c**d)%n

print("Decrypted:",x)