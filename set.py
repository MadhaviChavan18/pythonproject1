#create set
a={}
print(type(a))

#empty set
b=set()
print(type(b))

#set with value

'''c={a,10.2,'Madhavi',False}
print(type(c))
print(c)'''

#methods
#1)add()

c={10,50,20,"Madhu"}
print(c)
c.add("Bright")
print(c)

#2)update
d={'abc',10,10.5,False}
d.update("Python")
print(d)
d.update(["Python"])
print(d)

#3)pop()
g={10.2,200,'zxy',True}
g.pop()
print(g)

#4)remove()
h={10.2,56,89,75}
h.remove(10.2)
print(h)

#5)clear()
i={10,20,50,60,'xyz'}
i.clear()
print(i)

#mathamatics
#union(display all value in both set and not duplicate value repeated)

a1={10,20,50,'zcv',1.45}
b1={10,50,'ghj',50,300}
print(a1.union(b1))

#intersection(display commanvalues)
print(a1.intersection(b1))
print(a1 & b1)

#minus (for that use difference ())
print(a1.difference(b1))


c={a,10.2,'Madhavi',False}
print(type(c))
print(c)