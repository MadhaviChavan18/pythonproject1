# string
a="I Am python developer"
print(a)
print(a[7])#indexing
print(a[2:10])#slicing
print(len(a))#length
print(a[0:20])

print(a[0:15:3])#skipping character
print(type(a))

#isalnum

b="helloword"
print(b.isalnum())#alpha numeric value

c="i am"
print(c.isalnum())#space not consider in that method so it gives false ans

# endswith
print(c.endswith("am"))
print(c.endswith("iam"))

#count
x="Good morning"
print(x.count("o"))
print(x.count("a"))

#capitalize
d="madhu"
print(d.capitalize())

#find
print(x.find("r"))

#loewercase
print(x.lower())

#uppercase

print(d.upper())

#replace
y="That things is not good"
print(y.replace("is","are"))