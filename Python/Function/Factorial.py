def fact(a):
    prod=1
    for i in range(1,a+1):
        prod=prod*i
    print("Factorial of given number is:", prod)

fact(5)