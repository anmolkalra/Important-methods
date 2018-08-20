
print("Q1")
lst=[1,2,3,4,5]
print(list(reversed(lst)))

print("Q2")
s=input("Enter A string")
for i in range(len(s)):
    if s[i].isupper():
        print(s[i])

print("Q3")
s=input("Enter numbers").split(",")
lst1=[]
for i in s:
    lst1.append(int(i))
print(lst1)

print("Q4")
a=int(input("Enter A number"))
b=a
f=0
rev=0
while a!=0:
    f=a%10
    rev=rev*10+f
    a//=10
if b==rev:
    print("Palandromic Number")
else:
    print("Not a Palandromic Number")



print("Q5")
import copy
print("DeepCopy ")
l1 = ['a','b',['ab','ba']]

l2 = deepcopy(lst1)

l2[2][1] = "d"
l2[0] = "c";

print(l2)
print(l1)
print("Shallow Copy ")
l3=l1
lst3[0]="hi"
print(l3)
print(l1)
"""A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original."""
