#1
a=int(input("Enter your number:"))
if a>0:
    print("Positive")
else:
    print("Negative")
#2
a=int(input("Enter the value:"))
if a%2==0:
    print("Even number")
else:
    print("Odd number")
#3
a=int(input("Enter the base:"))
b=int(input("Enter the exponent:"))
result=a**b
print("The result is:", result)
#4
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
if a>b:
    print("A ia greater than B")
elif a<b:
    print("A is less than B")
else:
    print("Both are equal")
#5
year=int(input("Enter the year:"))
if year%4==0:
    print("Leap Year")
else:
    print("Non-leap Year")
#6
mark=int(input("Enter the mark:"))
if mark>90 and mark<100:
    print("Grade A")
elif mark>80 and mark<89:
    print("Grade B")
elif mark>70 and mark<79:
    print("Grade C")
elif mark>60 and mark<69:
    print("Grade D")
else:
    print("Grade F")
#7
age=int(input("Enter your age:"))
if age<16:
    print("You can't drive")
elif age>=16 and age<=17:
    print("You can drive but not vote")
elif age>18 and age<24:
    print("you can vote but not rent a car")
elif age>=25:
    print("You can do pretty much anything")
#8
for i in range (1,101):
    if i%3==0 and i%5==0:
        print(i,"FizzBuzz")
    elif i%3==0:
        print(i,"Fizz")
    elif i%5==0:
        print(i,"Buzz")   
    else:
        print(i)
#9
y=int(input("Enter the year:"))
if (y%4==0 and y%100!=0) or (y%400==0):
    print("Leap Year")
else:
    print("Not a leap year")
    