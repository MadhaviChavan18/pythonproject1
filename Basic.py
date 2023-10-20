a=1000
print(a)

#input and output operations

#for input= input()  for output=print()
# input from user x=input("Enter anyno")

x=input("Enter anyno")
print(x)

a=int(input("Enter the value:"))
print(a)
b=int(input("Enter the value:"))
print(b)

c=a+b
print(c)

d=float(input("Entre the value"))
print(d)
# display or know which type of variable

print(type(a))
print(type(d))
print(type(b))

#convert data in particular form use eval()
var=eval(input("Enter any thing"))
print(var)
print(type(var))
# keyword

import keyword
print(keyword.kwlist)