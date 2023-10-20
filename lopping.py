#loopnig means repeatation or itration

#while loop
'''i=1
while i<=5:
    print(i)
    i+=1

# print even no in between 0 to 10
n=0
while n<=25:
    if n%2==0:

        print(n)
    n+=1

# print od no in between 0 to 10
n=0
while n<=25:

    if n%2!=0:
        print(n)
    n+=1'''

# for loop
#for variable in list:

digit=[0,23,56]
for x in digit:
    print(x)
else:
    print("No more element in list")

#access string in for loop

for a in "Pythin":
    print(a)

# Display no using range ()

for a in range(10):
    print(a)

#Break
a=1
while a<=10:
    if a==5:
        break
    print(a)
    a+=1

fruits=["Apple","Banana","Cherry"]
for i in fruits:
    print(i)
    if i=="Banana":
       break

fruits=["Apple","Banana","Cherry"]
for i in fruits:

    if i=="Banana":
       break
    print(i)

#continue
a=1
for a in range(10):
    if a == 5:
        continue
    print(a)
    a+=1