#string programs

# no of words in a strings
"""""
sent=input("")
s=sent.split(" ")
count=0
for i in s:
    count+=1
print(count)
"""

#Frequency of all elements
"""""
word=input("")
store=[]
for i in  word:
    store.append(i)
for ch in set(store):
    print(f"{ch} occur {store.count(ch)} times ")
"""
#largest palindrome in a string 
"""""
sent=input("")
s=sent.split(" ")
store=[]

for i in s:
    if i[::-1]==i:
        store.append(i)
if store:
    max=store[0]
    for j in store:
        if len(j)>len(max):
         max=j
    print(max)
else:
   print("NO Palindrome")     
"""


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




#no.of words and sentences in  para
"""""
para=input("")
word=para.split()
end=["!","?","."]
prev=""
count=0
for i in para:
    if i in end and prev not in end:
        count+=1
print(f"Sentences:{count}")
print(f"Words:{len(word)}")
"""


# No of lines and words
"""""
para = ""

print("Enter your paragraph :")
while True:
    line = input()
    if line == "":
        break
    para += line + "\n"


lines = para.strip().split("\n")
line_count = len(lines)
words = para.split()
word_count = len(words)

print(f"Lines: {line_count}")
print(f"Words: {word_count}")
"""



#index of  a character in a string
"""""
strings=input("")
character=input("")
for i in range(len(strings)):
    if strings[i]==character:
        print(f"The {character} appears at an index of {i}")
"""






#alpha order and reverse
"""""
string=input("")
store=[]
for i in string:
    store.append(i)
store.sort()
print("Alphabetical Order:",end="")
for k in range(len(store)):
    print(store[k],end="")
print("")
store.reverse()
print("ReverseAlphabetical Order:",end="")
for j in range(len(store)):
    print(store[j],end="")
"""


#ismorphic
s=input("")
t=input("")
ran=min(len(s),len(t)-1)
for i in range(ran):
    if s[i]==s[i+1] and t[i]==t[i+1]:
        print("They are ismorphic")











#functions

