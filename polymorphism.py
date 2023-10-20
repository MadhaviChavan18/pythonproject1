#polymorphism

print(5+5)
print("5"+"5")
print(len("Ayush"))
print(len(["Ayush","Yash"]))

# types of plymorphism
#function overloading
class A:
    def show(self):
        print("Welcome")
    def show(self,first_name=''):
        print("welcome",first_name)
    def show(self,first_name,last_name=''):
        print("welcome",first_name,last_name)
obj=A()
obj.show(1)
obj.show('Madhavi')
obj.show('Madahvi','Chavan')

#overriding

class B:
    def display(self):
        print("this is the parent class method")

class C(B):
    def display(self):
        super().display()
        print("this is the child class method")
obj1=C()
obj1.display()
