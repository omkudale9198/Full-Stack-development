class A:
    def __init__(self,b):
        print("A class constructor")
        self.b=b

    def get(self):
        print("Get from class A")
        print("B:",self.b)

class B(A):
    def __init__(self,a,b):
        print("B class constructor")
        super().__init__(b)
        #A.__init__(self,b)
        self.a=a

    def put(self):
        print("Put from class B")
        print("A:",self.a)

obj=B(100,200)
obj.get()
obj.put()