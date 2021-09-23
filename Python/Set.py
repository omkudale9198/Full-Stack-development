login={
    "user1":{
        "username":"Omkar",
        "age":23,
        "mob":9876543210,
    },

    "user2":{
        "username":"Rajat",
        "age":26,
        "mob":9874563210,
    }
}

username=input("Enter username: ")
age=int(input("Enter age: "))
mob=int(input("Enter mob no. "))

flag=0
for i in login:
    if(login[i]["username"]==username and login[i]["age"]==age and login[i]["mob"]==mob):
        print(login[i])
        flag=1

if(flag==0):
    print("Given data does not match")

