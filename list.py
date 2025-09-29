#smallest Number in list
"""""
num_list=[7,2,5,7,2,90,1,23,4]
least=num_list[1]
for i in num_list:
    if i<least:
        least=i
print(f"The smallest number in the list:{least}")
"""


#difference between two list
"""""
list1=[1,3,6,88,90,4] 
list2=[2,5,7,2,97,6,13]
list3=[i for i in list1 if i not in list2]
print(list3)
"""

#intersection of list
"""""
list1=[1,2,4,578,8,79,6]
list2=[456,2,7,4,70,8,19]
list3=[i for i  in list1 if i  in list2]
print(list3)
"""



#union of list
"""""
list1=[1,2,4,578,8,79,6]
list2=[456,2,7,4,70,8,19]
list3=list1+list2
list3=set(list3)
print(list3)
"""


#fibonacci series and store in list
"""""
n=int(input(""))
fibonacci_list=[0,1]

for i in range(2,n):
    next_element=fibonacci_list[-1] + fibonacci_list[-2]
    fibonacci_list.append(next_element)
print(fibonacci_list)
"""


#largest subsequence in a list
"""""
def max_subsequence_sum(arr):
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

lst = [5, -2, 3, 4, -1, 2, -1, -5, 4]
print("Largest contiguous subsequence sum:", max_subsequence_sum(lst))
"""

#merge two sorted lists
"""""
list1=[1,3,64,8,69,26,58,10]
list2=[2,456,1,3,68,356,4]
list3=sorted(list1) + sorted(list2)
print(sorted(list3))
"""

#Remove even numbers from a list
"""""
list1=[1,2,3,4,5,6,8,12,24,6,90,133]
new_list=[]
for i in list1:
    if i%2!=0:
        new_list.append(i)
        
print(f"The list formed witout Even Numbers:{new_list}")
"""



#Max and Min element in a list
"""""
List=[1,2,4,566,46,4788,38,23]
max=List[0]
min=List[0]
for i in List:
    if i>max:
        max=i
    if i<min:
        min=i
print(f"The Max and Min Elements in a list: {max} and {min}")
"""



#shuffle elemnts in a list
"""""
import random

List=[1,2,46,345,78,4556,245,46,8]
random.shuffle(List)
print(f"Shuffled List: {List}")
"""


#ascending order lists
"""""
List=[1,2,46,345,78,4556,245,46,8]
List.sort()
print(List)
"""



#frequency of elements in list
"""""
List=[1,2,46,345,78,4556,245,46,8]

for i in set(List):
    print(f"{i} occur {List.count(i)} times.")
"""



# index of list
"""""
List=[1,2,46,345,78,4556,245,46,8]
n=int(input(""))
store=0

for i in List:
    if i==n:
        store=i
if store!=0:
      print(f"Index of number:{List.index(store)}")
else:
     print("The Number does not exist")
"""
#second largest number in list
"""""
List=[1,2,46,345,78,4556,245,46,8]
List.sort()
print(List[-2])
"""

#sorting  a list
"""""
l=[1,8,5,9,3,23,70]

for i in range(len(l)):
    m=i
    for j in range(i+1,len(l)):
        if l[j]<l[m]:
            m=j
    l[i],l[m]=l[m],l[i]
print(l)
"""











