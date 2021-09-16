a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
c=int(input("Enter 3rd Number: "))
d=int(input("Enter 4th Number: "))

largest=0

if(a>b and a>c and a>d):
    largest=a

if(b>a and b>c and b>d):
    largest=b

if(c>a and c>b and c>d):
    largest=c

if(d>a and d>b and d>c):
    largest=d

print("Largest number is", largest)