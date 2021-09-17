n=int(input("Enter a number: "))

temp=n
rev=0
d=0

while(n>0):
    d=n%10
    rev=rev*10+d
    n=n//10

if(temp==rev):
    print("Given nmber is Palindrome")
else:
    print("Give number is not a Palindrome")