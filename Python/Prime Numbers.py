lst=[2,4,6,7,11,7,13,15]

for i in range(len(lst)):
    flag=0
    for j in range(2,lst[i]):
        if(lst[i]%j)==0:
            flag=1
    if(flag==0):
        print(lst[i])