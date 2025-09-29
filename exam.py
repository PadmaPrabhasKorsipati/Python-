#matrix
"""""
list=[[1,2,3],[4,5,6],[7,8,9]]
sum=0
for i in list:
    for j in i:
      print(j,end=" ")
    print("\n")
    
print("\n")
for k in range(len(list)):
    print(list[k][k],end=" ")
   
    sum+=list[k][k]
print("\n")
print(f"The sum of diagonal:{sum}")

"""
#perfect number
""""
num=int(input(""))
sum=0
for i in range(1,num+1):
   if num%i==0 and i!=num:
      sum+=i
if sum==num:
   print("It is a perfect number")
else:
   print("It is not a perfect number")
"""



#tech number
"""""
num=input("")
first_num=int(num[:len(num)//2])
second_num=int(num[len(num)//2:])
total=first_num + second_num
if (total)**2==int(num):
    print("It is a Tech number")
else:
    print("It is not a Tech numnberr")
"""

#count sentences with a letter
"""""
sentence=input("")
s=sentence.split("...")
count=0
for i in s:
    i=i.strip()
    if len(i)>0 and i[0].lower()=="b":
        count+=1
print(count)
"""





#lcd of two numbers
"""""
num1=int(input(""))
num2=int(input(""))
lcd=max(num1,num2)
for i in range(lcd,num1*num2+1):
    if i%num1==0 and i%num2==0:
        lcd=i
        print(f"LCD of two Numbers:{lcd}")
        break
"""


#prime nummbers between two numbers
""""
num1=int(input(""))
num2=int(input(""))

for i in range(num1,num2+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i,end=",")
"""  

#GCD of two numbers
"""""
num1=int(input(""))
num2=int(input(""))
GCD=0
for i in range(1,max(num1,num2)):
    if num1%i==0 and num2%i==0:
        if i>GCD:
            GCD=i
print(f"The GCD of two numbers:{GCD}")
"""

#insert element
"""""
list=[1,2,3,5,6]
val=4
pos=4
list.insert(3,4)
print(list)
"""

#sum of factorial

"""""
n=int(input(""))
count=0

for i in range(1,n+1):
    mul=1
    j=i
    while j!=0:
        mul*=j
        j-=1
    count+=mul
print(count)
        
"""


#avg of +ve and -ve numbers until -1
"""""
psum=0
pnum=0
nsum=0
nnum=0
while True:
    n=int(input("Until(-1)input:"))
    if n==-1:
        break
    else:
        if n>0:
            psum+=n
            pnum+=1
        else:
            nsum+=n
            nnum+=1
if psum>0:
    paverage=psum/pnum
    print(f"The Average of +ve numbers:{float(paverage)}")
else:
    print("There are no +ve numbers")
if nsum>0 or nsum<0:
    naverage=nsum/nnum
    print(f"The Average of -ve numbers:{float(naverage)}")
else:
    print("The are no -ve numbers ")

"""

#method 2
"""""
text=input("")
s=text.split(",")
psum=0
pnum=0
nsum=0
nnum=0
for i in s:
    if int(i)==-1:
        break
    elif int(i)>0:
        psum+=int(i)
        pnum+=1
    else:
        nsum+=int(i)
        nnum+=1

if psum>0:
    paverage=psum/pnum
    print(f"The Average of +ve numbers:{float(paverage)}")
else:
    print("There are no +ve numbers")
if nsum>0 or nsum<0:
    naverage=nsum/nnum
    print(f"The Average of -ve numbers:{float(naverage)}")
else:
    print("The are no -ve numbers ")
"""


#sum of triangular numbers

"""""
n=int(input(""))
count=0
store=[]
for i in range(1,n+1):
    j=i
    add=0
    for j in range(1,i+1):
        add+=j
    store.append(add)

for k in store:
    mul=1
    while k!=0:
        mul*=k
        k-=1
    count+=mul
print(count)
"""



#right angled triangle
"""""
n=int(input(""))  
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("")
"""


#simple interest
"""""
principle_amount=int(input(""))
years=int(input(""))
gender=input("")
senior_citizen=input("")
if senior_citizen.lower()=="yes" and gender.lower()=="m":
    SI=(principle_amount*years*12)/100
    print(SI)
elif senior_citizen.lower()=="yes" and gender.lower()=="f":
    SI=(principle_amount*years*15)/100
    print(SI)
    
else:
      SI=(principle_amount*years*10)/100
      print(SI)
"""





#mean,median,mode

"""""
num=input("")
s=num.split(",")
count=0
snum=0
store=[int(i) for i in s]
store.sort()
for j in store:
    count+=j
    snum+=1
n=len(store)
if len(store)%2==0:
    median=store[int((((n/2)+(n/2+1))/2)-1)]
else:
    median=store[int((n+1)/2)-1]
print(median)
"""




#array
"""""
arr=[1,5,6,2,-3,-4,-2]
sum=0
for add in arr:
    sum+=add
arr.sort()
avg=sum/len(arr)
for i in range(len(arr)):
    if arr[i]<0:
        arr[i]=avg
print(arr)
"""

#difference
"""""
n=int(input(""))
tot=0
sum=0
for i in range(1,n+1):
    sum+=(i)**2
    tot+=i
diff=sum-(tot)**2
print(diff)
"""


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the number of terms: "))
print("Fibonacci series:")
for i in range(terms):
    print(fibonacci(i), end=" ")



def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibonacci(n)



n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


















