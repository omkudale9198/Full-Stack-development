class A:
    def get(self):
        self.x=100
        print("This is get from class A")

class B(A):
    def put(self):
        print("This is put from class B")
        print("X:",self.x)

class C(B):
    def display(self):
        print("display")
        print("X:",self.x)

obj=C()
obj.get()
obj.put()
obj.display()