#1
for i in range (1,11):
    print(i)
#2
for i in range(1,21):
    if(i%2==0):
        print(i)
#3
for i in range(1,21):
    if i%2!=0:
        print(i)
#4
a=int(input("Enter the value to find factorial:"))
fact=1
for i in range (1,a+1):
    fact*=i
print("The factorial is:",fact)
#5
sum=0
for i in range (1,101):
    sum+=i
print("Sum is:",sum)
#6
a=[10,20,30,40,50]
sum=0
for i in a:
    sum+=i
average=sum/5
print("Average=",average)
#7
print("SQUARE PATTERN")
n=5
for i in range(n):
    row=""
    for j in range(n):
        row+="*"
    print(row)


print("RECTANGLE PATTERN")
a=4
b=8
for i in range(a):
    row=""
    for j in range(b):
        row+="*"
    print(row)
#8
for i in range (1,6):
    print(i)
#9
for i in range(1,11):
    print(i)
#10
a=[10,20,30,40,10]
if a[0]==a[4]:
    print("True")
else:
    print("False")
#11
a=[3,5,9,15,34,75,66,90,89,100]
for i in a:
    if i%5==0:
        print(i)
#12
a=input("Enter a letter:")        
if len(a)==1 and a.isalpha():    
    if a in 'aeiou':
        print("Enter letter is a vowel")
    else:
        print("Enter letter is a consonent")   
else:
    print("Invalid input. Enter the single letter")
#13
even=[]
odd=[]
for i in range (10,56):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(len(even))
print(len(odd))
#14
for i in range(1,26):
    if i%5!=0:
        print(i)
#15
a=[2,4,6,8,10]
factorial=[]
for i in a:
    fact=1
    for j in range(1,i+1):
        fact*=j
    factorial.append(fact)
print(factorial)
#16
a=int(input("Enter the value for a:"))
b=int(input("Enter the value for b:"))
product=a*b
print("Product is:",product)
if product>500:
    print("Sum:",a+b)
else:
    print("Invalid")
#17
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")
#18
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
if a>b and a>c:
    print("a is greater than b and c")
elif b>c:
    print("b is greater than a and c")
else:
    print("c is greater than a and b")
#19
a=[23,4,-6,23,-9,21,3,-45,-8]
for i in a:
    if i>0:
        print(i,"Positive")
    else:
        print(i,"Negative")
