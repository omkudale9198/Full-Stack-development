'''
   *
  ***
 *****
*******
 *****
  ***
   *
'''

for i in range(1,5):
    for j in range(1,5-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

for i in range(3,0,-1):
    for j in range(1,4-i):
        print(" ", end="")
    for k in range(2*i,0,-1):
        print("*", end="")
    print()
