lst=[2,4,6,7,11,7,13,15]

n=int(input("Enter a number 5"))
flag=0

for i in range(len(lst)):

    if(n==lst[i]):
        flag=1
        break

if(flag==1):
    print("Exist")

else:
    print("Doesn't exist")


