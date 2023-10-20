class A:
    a=100 #public
    _b=200 #protected
    __c=None #private

    print(a," ",_b," ",__c)

class A1:
    a=100
    _b=200
    __c=None
    print(a, " ",_b," ",__c)
    def add(self):
        self.__c=self.a+self._b
        print("Addition=",+self.__c)
obje=A1()
obje.add()
print(obje.a)
print(obje._b)
print(obje.__c)
