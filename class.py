#senior citizen
"""
Age=int(input(""))
if Age>=60:
    print("Senior citizen")
else:
    print("Not a senior citizen")

"""


#positive or negative
""""
num=int(input(""))
if num>0:
    print("It is a positive number")
elif num<0:
    print("It is a negative number ")
else:
    print("The given number is zero")

"""
#even or odd
"""""
num=int(input(""))
if num%2==0:
    print("It is a even number")
else:
    print("It is a odd number")
    
"""
#distance  between two points 
"""""
x1=int(input(""))
x2=int(input(""))
y1=int(input(""))
y2=int(input(""))
distance=((x1-x2)**2+(y1-y2)**2)**1/2
print(f"The distance between two points is {distance}")
"""

#quadratic equations
""""
a=int(input(""))
b=int(input(""))
c=int(input(""))
d=(b**2-4*a*c)**0.5
root1=(-b+(d))/2*a
root2=(-b-(d))/2*a
print(f"The Roots of the equation are {root1} and {root2}")
"""
#looping statements

#while loop
"""""
a=int(input(""))
i=1
while i<=a:
    print(i)
    i+=1
"""


#sum of even numbers
"""""
num=int(input(""))
sum=0
i=1
while i<=num:
    if i%2==0:
        sum+=i

    i+=1
print(f"The sum of even numbers between 0 and {num} are {sum}")

"""

#sum of odd numbers
"""""
num=int(input(""))
sum=0
i=1
while i<=num:
    if i%2!=0:
        sum+=i

    i+=1
print(f"The sum of odd numbers between 0 and {num} are {sum}")

"""
#sum of digits in a number
"""""
num=int(input(""))
sum=0

while num!=0:
    r=num%10
    sum+=r
    num=num//10

print(f"The sum of digits in a number is {sum}")

"""


#Armstrong number
"""""
num=int(input(""))
first_num=num
sum=0
while num!=0:
    r=num%10
    sum+=r**3
    num=num//10

if sum==first_num:
    print(f"{first_num} is an Armstrong Number")
else:
    print(f"{first_num} is not an Armstrong Number")

"""


#palindrome
"""""
var=input("")
s=var[::-1]
if var==s:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
"""

#harshad number
"""""
num=int(input(""))
first_num=num
sum=0
while num!=0:
    rem=num%10
    sum+=rem
    num=num//10

if first_num%sum==0:
    print("It is a Harshad NUmber")
else:
    print("It is not a Harshad Number")
"""

#Happy Number
"""""
num=int(input(""))
first_num=num


def is_happy(n):
    sum=0
    while n!=0:
      rem=n%10
      sum+=rem**2
      n=n//10
      return sum
    
coll=set()

while num!=1 and num not in coll:
    coll.add(num)
    num=is_happy(num)
if num==1:
    print("It is a Happy Number")
else:
    print("It is a Not a Happy NUmber")

"""


#vowels or consonant
"""""
vowel=["a","e","i","o","u"]
vsum=0
csum=0

word=input("")
newword=word.lower()
for i in newword:
    if i in vowel:
        vsum+=1
    else:
        csum+=1
print(f"The no of vowles:{vsum}\nThe no of consonants:{csum}")
"""

#no of words
"""""
word=input("")
count=1
for i in word:
    if i==" ":
        count+=1
print(f"The no of words: {count}")

"""

#frequency of characters
"""""
word=input("")
newword=word.lower()

store=[]
for i in newword:
    store.append(i)

for ch in (set(store)): 
    print(f"{ch} appeared {store.count(ch)} times")
"""""

#find special characters 

"""""
sentence=input("")
s_char=["!","@","#","$","%","^","&","*","()","[]","<>","|",",",".","/","\\"]
count=0
for i in sentence:
     if i in s_char:
        count+=1
print(f"The No of Special Characters: {count}")
"""""

#remove duplicates in list
"""""
wdupli=[1,2,3,4,1,2,4,5]
Olist=[]
for i in wdupli:
    if i not in Olist:
        Olist.append(i)
print(Olist)
"""


   

#LCM of two Numbers
"""""
num1=int(input(""))
num2=int(input(""))
lcm=max(num1,num2)
for i in range(1,max(num1,num2)):
    if i%num1==0 and i%num2==0:
        lcm=i
        break
print(lcm)
"""

"""""
element=int(input(""))
list1=[1,2,3,1,1,5,9]
list2=[i for i in  list1 if element not in list1]
print(list2)
"""""










