#function
#def function name():

#default function
def message(): #function declaration
    print("Hello")
message() #function calling

#parameterised function
def message1(name):
    print("Hello morning" +name)
message1("Madhu")

#addition

def add(a,b):
    print("Addition=",a+b)
add(45,89)

#use of return keyword

def square(num):
    return num**2
ob=square(5)
print("square of givenno is:",ob)

#string lenth()

def a(string):
    return len(string)
print("length of given string is:",a("Welcome madhu"))
print("length of given string is:",a("We aaer happy"))
print("length of given string is:",a("try to catch your vision"))
print("length of given string is:",a("always full wth hope"))
print("length of given string is:",a("always be positive"))

#lambda function

x=lambda a: a+10
print(x(5))
y=lambda a,b:a*b
print(y(58,98))

z=lambda a,b,c:a+b+c
print(z(56,879,165))

def abc(n):
    return lambda a:a*n
x=abc(2)
print(x(11))
