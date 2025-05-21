#1
def sayHello(name):
    print("Hello, World!")
    print("Hello,",name)    
sayHello("Monica!")
#2
x=10
y=10
def add(a,b):
    c=a+b
    print("Sum is:",c)
add(x,y)
#3
a=15
b=10
def multiply(x,y):
    c=a*b
    print("Multiply of 2 number is:",c)
multiply(a,b)
#4
def multiply(a,b):
    c=a*b
    print("Answer is:",c)
multiply(5,5)
#5
def divide(a,b):
    c=a/b
    print("Answer is:",c)
divide(20,5)
#6
a=int(input("Enter a value to find factorial:"))
def factorial(n):
    if n<0:
        print("Invalid. Enter the positive number")
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(f"Factorial is:{factorial(a)}")
#7
def square():
    a=5
    print("Square of given number:", a**2)
square()