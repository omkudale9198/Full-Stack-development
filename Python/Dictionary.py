login={
    "user1":{
        "username": "Omkar",
        "age":23,
        "mob":9876543210,
    },

    "user2":{
        "username": "Rajat",
        "age":25,
        "mob":9873216540,
    }
}

user=input("Enter Username: ")
age=int(input("Enter age: "))
mob=int(input("Enter number:"))

flag=0

for i in login:
    if(login[i]['username']==user and login[i]['age']==age and login[i]["mob"]==mob):
        print(login[i])
        flag=1

if(flag==0):
    print("Entered data doesn't match")