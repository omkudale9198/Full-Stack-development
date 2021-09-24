class A:
    def get(self):
        print("This is get from class A")

class B(A):
    def put(self):
        print("This is put from class B")

obj=B()
obj.get()
obj.put()