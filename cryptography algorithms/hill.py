p=input("plain:").upper().replace(" ","")

k=[[9,4],[5,7]]

if len(p)%2:
    p+="X"


e=""

for i in range(0,len(p),2):
    x=ord(p[i])-65
    y=ord(p[i+1])-65

    a=(k[0][0]*x + k[0][1]*y)%26

    b=(k[1][0]*x + k[1][1]*y)%26

    e+=chr(a+65) + chr(b+65)

print("Encrypted:",e)