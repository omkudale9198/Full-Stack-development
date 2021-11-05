class A:
    def get(self):
        self.x=100
        print("This is get from class A")

class B:
    def get(self):              #ambiguity
        self.y=100
        print("This is put from class B")

class C(A,B):
    def display(self):
        print("Display")
        print("X:", self.x)
        #print("Y:", self.y)

obj=C()
obj.get()
obj.display()
