import mysql.connector as ms

con=ms.connect(host="localhost", user="root", password="1234", database="db1")
mycursor=con.cursor()

def insert():
    eid=int(input("Enter your id: "))
    ename=input("Enter your name: ")
    eloc=input("Enter your location: ")
    edesi=input("Enter your Designation: ")
    esal=int(input("Enter your salary: "))


    q="insert into employee values(%s,%s,%s,%s,%s)"
    val=(eid,ename,eloc,edesi,esal)
    mycursor.execute(q,val)

    con.commit()
    print("Record inserted...")


'''
mycursor.execute("create databse, mynewdb")
'''

def display():
    mycursor.execute("select * from employee")
    data=mycursor.fetchall()

    print("-----------------Given Data------------------")
    print("eid-ename-----eloc-----edesi-------------------esal------")

    for i in data:
        print(i[0]," ",i[1]," ",i[2]," ",i[3]," ",i[4])

def delete():
    eid=int(input("Enter Eid for delete: "))
    q="delete from employee where eid=%s"
    val=(eid,)
    mycursor.execute(q,val)
    con.commit()
    print("Record Deleted...")

n=1
while(n!=0):
    n=int(input("1: insert \n2:Display \n3: Delete \n4:Exit \n "))
    if(n==1):
        insert()
    elif(n==2):
        display()
    elif(n==3):
        delete()
    else:
        n=0

else:
    print("-------Thanks for visiting--------")

