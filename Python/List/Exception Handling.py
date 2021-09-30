"""
a=int(input("Enter Numerator: "))
b=int(input("Enter Denmoniator "))
"""
'''
try:
    c=a/b
    print("Division:",c)

except Exception as e:
    print(e)
'''

"""
try:
    c=a/b
    print(c)

    try:
        print(x)
    except Exception as e:
        print(e)

except Exception as e:
    print(e)

finally:
    print("Rest of the program")
"""

'''
try:
    c=a/b
    print(c)

    try:
        print(x)
    except(NameError):
        print("NameError")


except(ArithmeticError):
    print("ArithmeticError")

except(NameError):
    print("NameError")
'''

try:
    age=int(input("Enter your age: "))

    if(age<18):
        raise ValueError
    else:
        print("Eligible for voting")

except ValueError:
    print("Not Eligible")