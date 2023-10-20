# how to creat a list
# dreate empty list
a=[]
print(type(a))

# create list with value
b=[10,"Bright",True,10.2,'Madhavi',10.2]
print(b)

# Another method for list declaration
c=list()
print(c)
print(type(c))


# indexing of list
d=[100,'Aayush',True,10.5,'Ayush',100]
print(d[0])
print(d[1])
print(d[5])

#oerder list checking
a=[1,2,"Bright",30.5,"xyz",5,6]
b=[1,2,5,"Bright",30.5,"xyz",6]
print(a==b)

#slicinng for list

b2=[1,2,3,4,5,6,7,8]
print(b2[3])
print(b2[3:7])

# changes in list
b2[3]=100
print(b2)
#operation on the list
# 1)repetation
c3=[100,'A',"Madhavi",20.1]
r=c3*2
print(r)

#2)concatenation
c4=[100,500,10000,'B']
con=c3+c4
print(con)

#3)Display length of element
print(len(c4))

#4)ittration(loop)
list12=[22,90,100,1]
print(list12)
for i in list12:
    print(i)

#5)Membership
#it returns true if a particular item exist in particular list atherwise false
list1=[100,200,300,700,800]
print(100 in list1)
print(5000 in list1)

#index value

s=[10,'a',100,200]
print(s[1])
print(s[-1])

#Methods of list
#1)count()

s=[10,20,"Madhavi",'a',10,"Madhavi",10]
print(s.count(10))
print(s.count("Madhavi"))
print(s.count(20))

#2)index()
print(s.index('a'))

#3) insert()
print(s)
s.insert(2,'Python')
print(s)

#4) pop() (for delete operation use the pop())
print(s)
s.pop(2)
print(s)

#without giving index value pop() method deleted last value
s.pop()
print(s)

#5)extend() for adding two list
a1=[10,20,30,60]
b1=[-1,500,'s',600]
a1.extend(b1)
print(a1)

#6)copy()

a3=[]
a3=a1.copy()
print(a3)
#7)sorting

d1=[10,20,50,8000,-2]
d1.sort()
print(d1)

d1.sort(reverse=True)
print(d1)

#8)reverse()
d2=[10,20,-8,65]
d2.reverse()
print(d2)

#9)nestedlist()
d3=[10,50,48,['a','b','c',[-1,-8,-71]]]
print(d3)

#10) list comprention
d4=['Madhavi','Amol','Umesh','Aarohi']
d5=[word for word in d4 if word.startswith('A')]
print(d5)

#11) list unpacking

z=["Umesh","Ramesh"]
n1,n2=z
print(n1)
print(n2)
print(z)
