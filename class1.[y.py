#oop's cocepts
#class

class emp: #class declaration
    a=100
    def getdata(self):
        print("we are in class")
obj=emp()
obj.getdata()
print(obj.a)

class xyz:
    a=10
    b=56
    def add(self):
        c=self.a+self.b
        print("Addition of nos=",c)
    def positive(self):
        if self.a>0:
            print("No is positive")
        else:
            print("No is negative")
obj=xyz()
obj.add()
obj.positive()

#constructor
class A:
    def __init__(self):
        print("constructor")
obj1=A()

class A1:
    def __init__(self):
        name="Madhu"
        print(name)
    def a(self):
        print("Hello")
obj2=A1()
obj2.a()

class B:
    a=10
    def __init__(self):
        name="Madhu"
        print(name," ",self.a)
obj3=B()

# we declare multiple costructor but get only last one constructor output
class c:
    def __init__(self):
           print("hi...")
    def __init__(self):
        print("Hello...")
    def __init__(self):
        print("How are you")
obj4=c()

class ABc:
    "Learn Python"
    a=10
    print(a)
ob1=ABc()
print(ob1.a)
print(ABc.__doc__)

#parametrized constructor

class X:
    def __init__(self,age,name,address):
        print(age,name,address)
ob2=X(10,"Aarohi","Pune")

