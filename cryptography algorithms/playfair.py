key=input("Enter Key:").upper().replace("J","I")

p=input("Enter text:").upper().replace("J","I")

s=""

for c in key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if c not in s:
        s+=c


m=[s[i:i+5] for i in range(0,25,5)]

def  pos(c):

    for i in range(5):

       for j in range(5):
           if m[i][j]==c:
               return i,j


x=""

i=0;

while(i<len(p)):

    a=p[i]

    b=p[i+1] if i<len(p) else "X"

    if a==b:
        x+=a+"X"
        i+=1


    else:
        x+=a+b

        i+=2

if len(x)%2:

    x+="X"



e=""

for i in range(0,len(x),2):
    a=x[i]
    b=x[i+1]
    r1,c1=pos(a)
    r2,c2=pos(b)

    if r1==r2:
        e+=m[r1][(c1+1)%5] + m[r2][(c2+1)%5]

    elif c1==c2:

        e+=m[(r1+1)%5][c1] + m[(r2+1)%5][c2]

    else:

        e+=m[r1][c2] +m[r2][c1]

print("Encrypted:",e)





