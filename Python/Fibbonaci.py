a = 0
b = 1
f = 1
n = int(input("How many fibbonaci numbers you want? "))

for i in range(n):
    f = a+b
    a = b
    b = f
    print(a)