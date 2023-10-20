#single inheritance

class A:
    a=10
    name="Aarohi"
    def getdata(self):
        print(self.a," ",self.name)
class B(A):
    b=20
    name1=("Madhavi")
    def putdata(self):
        print(self.b," ",self.name1)
obj=B()
obj.getdata()
obj.putdata()

#multilevel inheritance
class add:
     a=20
     b=36
     def add1(self):
         print(self.a+self.b)

class sub(add):
    c=56
    d=89
    def sub1(self):
        print(self.c-self.d)
class mult(sub):
    e=45
    f=89
    def mult1(self):
        print(self.e*self.f)

obj1=mult()
print(obj1.a)
print(obj1.b)
print(obj1.c)
print(obj1.d)
print(obj1.e)
print(obj1.f)
obj1.sub1()
obj1.add1()

obj1.mult1()

#multiple inheritance

class  cal1:
    def sum(self,a,b):
        return(a+b)
class  cal2:
    def sub(self,a,b):
        return (a-b)
class cal3(cal1,cal2):
    def mul(self,a,b):
        return (a*b)
obj2=cal3()
print(obj2.sub(90,89))
print(obj2.sum(56,74))
print(obj2.mul(85,60))

#issubclass()
class A:
    a=20
    print(a)
class B(A):
    b=60
    print(b)
class C(B):
    c=56
    print(c)
c1=C()
print(issubclass(C,B))
print(issubclass(B,C))
print(issubclass(B,A))
print(issubclass(A,B))

#hybrid/hierachy  inheritance
class father:
    surname="Patil"
    def getdata(self):
       print("surname is=",self.surname)
class son1(father):
    name="Ganesh"
    def putdata(self):
        print("name is=",self.name)
class  son2(father):
    name="ayush"
    def display(self):
         print("name is=",self.name)
obj4=son1()
print(obj4.putdata())
print(obj4.getdata())
obj5=son2()
print(obj5.getdata())
print(obj5.display())