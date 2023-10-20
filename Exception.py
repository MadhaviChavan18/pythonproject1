a=10
b=0
try:
     c=a/b
     print(c)
except:
    print("Exception handled")

x=int(input("Enetr no"))
y=int(input("Enter no"))
try:
    z=x/y
    print("result",z)
except:
    print("Can not divide by zero")
    print("Hello we are in Excetion")