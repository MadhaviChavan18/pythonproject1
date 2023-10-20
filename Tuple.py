#create Tuple

var=()
print(type(var))

#create tuple with value
a=(1,2,3,4,5)
print(a)

b=(1,2,3,5.4,9.5,'a','b',"Raj",1,9.5,'a')
print(b)
#tuple declare also like
c=1,2,5,'n',"Madhu"
print(c)
print(type(c))

d=12
print(d)
print(type(d))
e=10,
print(e)
print(type(e))

#methods for tuple
#1) len()
f=(1,2,3,40,80,78)
print(f)
print(len(f))

#copy()
g=f
print(g)

'''#immutable in nature
g=(12,5,6,8,45,74)
g[2]='a'
print(g)'''

#indexing
j=(12,52,68,9,5,'a')
print(j[1])

#Append (add eleemnet)

k=(1,2,3,5,'a')
k.append("Madhu")
print(k)
#we can not do addition,isertion,deletion operation in tuple