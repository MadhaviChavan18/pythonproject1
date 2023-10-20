#conditional staement

#if condition

var1=1000
if var1>=100:
    print("No is too large")
#user input
# if
user_input=eval(input("Enter any no"))
if user_input>=0:
    print("no is positive")

#if else

n=eval(input("Enter no"))
if n>=0:
    print("No is oositive")
else:

    print("No is negative")

#Even odd no
n=eval(input("Enter no"))
if n%2==0:
    print("No is Even")
else:
    print("No is Odd")

# no is divisible by 5 & 10
num1=eval(input("enter the no"))
if num1%5==0 and num1%10==0:
    print("No is Divisible")
else:
    print("No is not Divisible")

# Given chracter is vowel or consonents
d=str(input("Enter any character"))
if d=='a' or d=='e' or d== 'i' or d=='o' or d=='u' or d=='A'or d=='E' or d=='I' or d=='O' or d=='U':
    print("character are vowel")
else:
    print("character is conosenents")


