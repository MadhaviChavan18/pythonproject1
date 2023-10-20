#create Dictionary

a1={}
print(type(a1))

a={"name":"Madhavi"}
print(a)

b={"nmae":"Madhu","age":"25","phone no":"4587312155"}
print(b)

#Dictionary methods
#pop()
var1={"Name":"xyz","age":"20","user name":"Ayush"}
print(var1)
var1.pop("Name")
print(var1)

#get()
var2={"Nmae":"Abc","age":"20","password":"abc@123","address":"Pune"}
print(var2.get("password","This key is not correct"))

#clear()
var3={"Nmae":"Abc","age":"20","password":"abc@123","address":"Pune"}
print(var3)
var3.clear()
print(var3)

#key()
var4={"Nmae":"Abc","age":"20","password":"abc@123","address":"Pune"}
print(var4)
print(var4.keys())

#values()
var5={"Nmae":"Abc","age":"20","password":"abc@123","address":"Pune"}
print(var5)
print(var5.values())
print(var5)

#items()
var6={"Nmae":"Abc","age":"20","password":"abc@123","address":"Pune"}
print(var6)
print(var6.items())

#changing values
var6["age"]=2
print(var6)

#with for loop and use the sepration symbol
var4={"Nmae":"Abc","age":"20","password":"abc@123","address":"Pune"}

for keys,values in var4.items():
    print(keys,values,sep='-->')

