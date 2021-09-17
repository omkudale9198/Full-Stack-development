p1=int(input("Price of 1st product: "))
p2=int(input("Price of 2nd product: "))
dist=int(input("Enter distance: "))
fare=0
total=0

if(dist<3):
    fare=10
elif(dist<6):
    fare=20
else:
    fare:30

total=dist*fare+p1+p2

print("Total amount of bill is: ", total)