#reverse string using recursive funcction
"""""
def reverse_string(word):
    if len(word)<=0:
        return word
    else:
        return (word[1:]) +word[0]
text=input("")
print(f"Before Reverse: {text}")
print(f"After Reverse: {reverse_string(text)}")
"""
#valid password
"""""
def password_check(password):
    strength=0
    has_upper=has_lower=has_digit=has_special=False
    special=["!","@","#","$","%","^","&","*","()","[]","<>","|",",",".","/","\\"]
    for i in password:
        if i.isupper():
            has_upper=True
        elif i.islower():
            has_lower=True
        elif i.isdigit():
            has_digit=True
        elif i in special:
            has_special=True
    if has_lower and has_upper:
        strength+=1
    if has_digit:
        strength+=1
    if has_special:
        strength+=1


    if strength>=2:
        print("Password is valid")
    else:
        print("Password is invalid")
Your_Password=input("")
print(password_check(Your_Password))

"""

#Area of circle
"""""
Radius=float(input(""))
Area=3.14*((Radius)**2)
print(f"The Area of the Circle is {Area:.2f}")
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



#Average of list of numbers
"""""
List=input("")
s=List.split(",")

numbers=[ float(i) for i in s ]

sum=0
num=0
for i in numbers:
    sum+=i
    num+=1
Average=sum/num
print(f"The Average of the given numbers:{Average:.2f}")

"""

#perfectc square
"""""
number=int(input(""))
count=0
for i in range(1,number):
    if number==i*i:
        count=1
if count==1:
    print("The Number is a Perfect square")
else:
    print("The Number is not a Perfect Square")

"""


#largest prime number less than given number
"""""
number=int(input(""))

for i in range(1,number):
    if 
"""

