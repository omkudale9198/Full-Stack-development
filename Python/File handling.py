'''
handle=open("test.text","w")
handle.write("This file is created by me")
print("file created...")
handle.close()
'''
'''
handle=open("test.text","a")
handle.write("This is appended")
print("File appended")
handle.close()
'''
'''
handle=open("test.text","r")
#print(handle.read())

for x in handle:
    print(x)
    
'''


