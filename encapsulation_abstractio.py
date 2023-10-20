#encapsulation

class A:
    _a=10
    __b=60
    def show(self):
        print("a=",self._a)
        print("b=",self.__b)
obj=A()
obj.show()
print("outside the class",obj._a)
#print("outside class",obj.__b)
