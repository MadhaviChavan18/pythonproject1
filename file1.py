# create file
#obj_file=open("C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\abc.txt","x")
#print("File created successfully")

#write data inside file
obj_file=open("C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\abc.txt","w")
#print(obj_file.write("hello python i am on the way reach out you"))
#print(obj_file.write())

#read the data
obj_file=open("C:\\Users\\Admin\\PycharmProjects\\pythonProject1\\abc.txt","r")
print(obj_file.read(17))
#print the data line by line
print(obj_file.readline())
#print all data
print(obj_file.readlines())