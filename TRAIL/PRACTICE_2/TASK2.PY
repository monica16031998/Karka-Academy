#1
userName=input("Enter the username:")
pass_word=int(input("Enter your password:"))
print("Your Username is:", userName)
print("Your Password is:", pass_word)
#2
a=50
b=50
c=a+b
print("Sum of 2 value:", c)
#3
r=5
area=3.14*r**2
print("Area of Circle is:", area)
#4
length=int(input("Enter the value of length:"))
width=int(input("Enter the value of width:"))
print("Area of rectangle is:", length*width)
#5
b=int(input("Enter the value of base:"))
h=int(input("Enter the value of height:"))
area=(b*h)/2
print("Area of triangle is:", area)
#6
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print("Addition of given value:", a+b)
print("Subtraction of given value:", a-b)
print("Multiplication of given value:", a*b)
print("Division of given value:", a/b)
#7
a=50
a+=10
print(a)
a-=30
print(a)
a*=5
print(a)
a/=10
print(a)
#8
a=50
a+=30
print(a)
a-=30
print(a)
#9
a=20
b=30
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
#10
a=15
b=25
print(a>b and a<b)
print(a>b or a<b)
#11
a=10
b=20
c=a
a=b
b=c
print("a=",a)
print("b=",b)
a,b=10,20
a,b=b,a
print("a=",a)
print("b=",b)
#12
a=int(input())
b=int(input())
c=int(input())
print("Average is:", (a+b+c)/2)
#13
a=10
b=30
c=12
d=3
add=a+b
multiply=add*12
divide=multiply/3
print("Add:", add)
print("Multiply:", multiply)
print("Divide:", divide)
#14
a=int(input("Enter the Tamil subject mark:"))
b=int(input("Enter the English subject mark:"))
c=int(input("Enter the Maths subject mark:"))
d=int(input("Enter the Science subject mark:"))
e=int(input("Enter the Social subject mark:"))
total=a+b+c+d+e
average=total/5
print("Total marks =", total)
print("Average =", average )