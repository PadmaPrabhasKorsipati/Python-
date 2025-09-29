'''Year=int(input(""))
def is_leap(year):
   if (year%4==0 and year%100!=0) or year%400==0:
    print(True) 
   else:
    print(False)
is_leap(Year)'''


'''n=int(input(""))
for i in range(1,n+1):
    print(i)'''


'''name=input("")
string=name.lower()
vowel_count=0
for x in string:
    if x in ["a","e","i","o","u"]:
        vowel_count +=1
        
print(vowel_count)'''








'''name=input("")
s=len(name)
print(s)'''




'''string=input("")
rep=input("")
count=0
for char in string:
    if char==rep:
        count+=1
print(count)'''


'''given=input("").split(" ")
for i in given:
    print(i.upper())'''



'''i=int(input(""))
j=int(input(""))
k=int(input(""))
n=int(input(""))
coordinate=[(i,j,k)for i in range(i+1)
for j in range(j+1)
for k in range(k+1)
if (i+j+k)!=n]
print(coordinate)'''


#factorial
def factorial(n):
    mul=1
    while i!=0:
        mul*=i
        i-=1
    print(mul)

num=int(input(""))
factorial(num)












