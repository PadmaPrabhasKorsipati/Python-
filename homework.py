
'''''
Agegroup=int(input(""))
if Agegroup<=5:
    print("The ticket price is Free")
elif Agegroup<=18:
    print("The ticket price is Rs100")
elif Agegroup<=60:
    print("The ticket price is Rs200")
else:
    print("The ticket price is Rs50")
    
'''''''''



'''

number=int(input(""))
if number>0 and number%2==0:
    print("The given number is positive and even")
elif number>0 and number%2!=0:
    print("The given number is positive and odd  ")
elif number<0 and number%3==0:
    print("The given number is negative and divisible by 3 ")
else:
    print("zero")
    
'''

'''
math=int(input(""))
physics=int(input(""))
chemistry=int(input(""))

total=math+physics+chemistry

percentage=total/300*100

if percentage>90:
    print("The grade is A+")
elif percentage>=75:
    print("The grade is A")
elif percentage>=50:
    print("The grade is B")
else:
    print("Fail")

'''


''''

Units=int(input())
if Units<=50:
      print(f"Electricity Bill={Units*3}Rs")
elif Units<=150:
    print(f"Electricity Bill={(50*3)+((Units-50)*5)}")
else:
    print(f"Electricity Bill={(50*3)+(100*5)+((Units-150)*8)}")


'''








'''''
c=input("")
if c.isalpha():
    c=c.lower()
    if c=='a'or c=='e' or c=='i' or c=='o' or c=='u':
        print("It is a Vowel.")
    else:
        print("It is a Consonant.")   

else:
    print("It is not a Alphabet")

'''''''''





''''
year=int(input())
if (year%4==0 and year%100!=0) or (year%400==0):
    print("It is a leapyear")
else:
    print("It is not a leap year")

'''





''''
number=int(input())
if number%5==0 and number%11==0:
    print("It is divisible by both 5 and 11")
else:
    print("It is Indivisible")

'''





'''''
input=input("")
a,b,c=input.split(",")
x=int(a)
y=int(b)
z=int(c)
if x>y and x>z:
    print(f"larget number is {x}")
elif y>x and y>z:
    print(f"largest number is {y}")
else:
    print(f"Largest number is {z}")

'''




''''
number=int(input(""))
if number>0:
    print("It is a positive number")
elif number<0:
    print("It is a Negative number")
elif number==0:
    print("It is Zero")

'''




''''
year=int(input("Enter the Year"))
month=int(input("Enter month (1-12)"))
if month<1 or month>12:
    print("Invalid month")
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("No of Days=31")
elif month in [4, 6, 9, 11]:
    print("No of Days=30")
elif month in [2]:
    if (year%4==0 and year%100!=0) or (year%400==0):
        print("No of Days=29")
    else:
        print("No of Days=28")

'''





'''''
x=int(input(""))
y=int(input(""))
if x>0 and y>0:
    print(f"Point ({x},{y}) lies in first quadrant")
elif x<0 and y>0:
    print(f"Point ({x},{y}) lies in Second quadrant")
elif x<0 and y<0:
    print(f"Point ({x},{y}) lies in third quadrant")
elif x>0 and y<0:
    print(f"Point ({x},{y}) lies in fourth quadrant")
elif x==0 and y>0:
    print(f"Point ({x},{y}) lies in +ve y-axis")
elif x==0 and y<0:
    print(f"Point ({x},{y}) lies in -ve y-axis")
elif x>0 and y==0:
    print(f"Point ({x},{y}) lies in +ve x-axis")
elif x<0 and y==0:
    print(f"Point ({x},{y}) lies in -ve x-axis")
else:
    print(f"Point ({x},{y}) lies in horizon")

'''






''''
input=input("")
a,b,c=input.split(",")
angle1=int(a)
angle2=int(b)
angle3=int(c)
if angle1>0 and angle2>0 and angle3>0 and (angle1+angle2+angle3==180):
    print("It is a valid Traingle")
else:
    print("It is a invalid triangle")

'''







'''
value=input("")
Target=int(input(""))
a,b=value.split(",")
num1=int(a)
num2=int(b)
x=Target-num1
y=Target-num2
p=abs(x)
q=abs(y)
if p>q:
    print(f"The nearest value is {num2}")
else:
    print(f"The nearest value is {num1}")

'''


''''
Date=input("")
day,month,year=Date.split("-")
day=int(day)
month=int(month)
year=int(year)
if month<1 or  month>12:
    print("Invalid month")
if month in [1, 3, 5, 7, 8, 10, 12]:
    if day>0 and day<32:
        print("The Date is valid")
    else:
        print("The Date is invalid")

elif month in [4, 6, 9, 11]:
    if day>0 and day<31:
        print("The Date is valid")
    else:
        print("The Date is invalid")
elif month in [2]:
    if (year%4==0 and year%100!=0) or (year%400==0):
        if day>0 and day<30:
            print("The Date is valid")
        else:
            print("The Date is invalid")
    else:
        if day>0 and day<29:
            print("The Date is valid")
        else:
            print("The Date is invalid")

'''


 



''''''''''
N=int(input(""))
i=1
sum=0
while i<=N:
    sum+=i
    print(f"sum of first {N} numbers={sum}")
    i+=1
'''''''''


'''''
m=int(input(""))
for i in range(10,0,-1):
    print(f"{m}x{i}={m*i}")

'''







'''''
N=int(input(""))
i=1
factorial=1
while i<=N:
    factorial*=i
    print(factorial)
    i+=1

'''











'''''
start=int(input(""))
end=int(input(""))
print(f"The numbers divisible by 5 from{start} and {end}")
for i in range(start,end+1):
    if i %5==0:
        print(i)

'''''







'''''
number=int(input("") )
print("The Prime Numbers are ")
for i in range(0,number):
    if i%2==0:
      print(i)

'''''












'''''
number=input("")
evennumbers=0
oddnumbers=0

for i in number:
    if i.isdigit():
        if int(i)%2==0:
        
            evennumbers+=1
        else:
            
            oddnumbers+=1
print(f"Even numbers:{evennumbers}")
print(f"Odd nubers:{oddnumbers}")

'''''
      







'''''
N=int(input(""))
oddnumbers=0
sum=0
for i in range(0,N):
    if i%2!=0:
        oddnumbers+=i

print(f"The sum of odd numbers upto N is {oddnumbers}")
       
'''








#Date=07-02-2025





'''age=int(input(""))
if age>=18:
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")'''







'''inp=input("").split(",")
numbers=[int(item) for item in inp] 
even_count=0
odd_count=0
for i in numbers:
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print(f"Even count={even_count}\nOdd count={odd_count}")'''







'''money=int(input(""))
if money%100==0:
    print(f"The withradawl money:{money}")
else:
    print("Invalid")'''




'''input=input("")
def abbreviator(name):
    a,b,c=name.split(" ")
    print(f"{a[0]} {b[0]} {c} ")
abbreviator(input)'''








'''word=(input(""))
if word==word[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")'''








'''ticket_price=int(input(""))
if ticket_price<5:
    print("The ticket price=Free")
elif ticket_price<=12:
    print("The ticket price=100")
elif ticket_price<=59:
    print("The ticket price=200")
else:
    print("The ticket price=150")'''






'''inp=input("").lower()
word=inp.split()

wordcount={}

for i in word:
    if i in wordcount:
        wordcount[i]+=1
    else:
        wordcount[i]=1
    
for i,count in wordcount.items():
    print(f"{i}:{count}")'''







'''speed=int(input(""))
if speed>60:
    print(f"Fine={(speed-60)*100}Rs")'''








n=int(input(""))
for i in range(0,n):
    if i<n:
        print(i**2)
    else:
        print("invalid")









