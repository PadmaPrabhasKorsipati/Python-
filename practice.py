#decimal and integers
"""""
d=input("")
x,y=d.split(".")
print(f"INT={x},DECIMAL={y}")
"""


#A AND B PRIME
"""""
A=int(input(""))
B=int(input(""))
store=[]
for i in range(A+1,B+1):
    count=0
    if i>1:
     for j in range(1,i):
        if i%j==0:
           count+=1
    if count>2:
       store.append(i)
for k in store:
   print(k,end=" ")
"""




#perfect number
"""""
n=int(input(""))
count=0
for i in range(1,n):
    if n%i==0:
        count+=i
if count==n:
    print("It is a perfect number")
else:
    print("It is not a Perfect Number ")
"""
#triplets
"""""
A=input("Enter upper limit:")
c=0
m=2
if A.isnumeric():
    x=int(A)
    while(c<x):
        for n in range(1,m+1):
            a=m*m-n*n
            b=2*m*n
            c=m*m+n*n
            if(c>x):
                break
            if(a==0 or b==0 or c==0):
                break
            print(a,b,c)
        m=m+1
else:
    print("invalid input")
"""
#Armstrong Number
"""""
num=int(input(""))
count=0
temp=num
while temp>0:
    digit=temp%10
    count+=(digit)**3
    temp=temp//10
if count==num:
    print("It is a Armstrong Number")
else:
    print("Not a Armstrong Number")
"""


#harshad number
"""""
num=int(input(""))
count=0
temp=num
while temp>0:
    digit=temp%10
    count+=digit
    temp=temp//10
if num%count==0:
    print("It is a Harshad Number")
else:
    print("It is not a Harshad Number")
"""

#happy Number
"""""
def happy(n):
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum=digit**2+sum
        temp=temp//10
    return sum
    
# Main Program

num=int(input("Enter the number:"))
result=num
while result!=1 and result!=4:
    result=(happy(result))
if result==1:
    print("True")
elif result==4:
    print("False")

"""


#Tech Number
"""""
num=int(input(""))
m=str(num)
a=m[:len(m)//2]
b=m[len(m)//2:]
c=int(a)+int(b)
d=c**2
if num==d:
    print("It is a Tech NUmber")
else:
    print("Not a Tech Number")
"""
#sq num and cub num
"""""
num=float(input(""))
sq=(num)**2
cub=(num)**3
print(f"{sq:.2f},{cub}")
"""

#matrix
"""""
li1=[[1,2],[4,5]]
li2=[[9,8],[6,5]]
li3=[[1,1],[1,1]]
for i in range(len(li1)):
    for j in range(len(li2)):
        li3[i][j]=li1[i][j] * li2[i][j]
for k in li3:
    for m in k:
        print(m,end=" ")
    print(" ")

"""

X=[[1,2],
   [5,3]]
Y=[[2,3],
   [4,1]]
result=[[0,0],
        [0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
