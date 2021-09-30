class Android:
    def camera(self):
        print("2mp camera...")

class Samsung(Android):
    def camera(self):
        print("10mp camera...")

class Nokia(Android):
    def camera(self):
        print("12mp camera...")

    def call(self):
        print("Call by Nokia...")

        
obj=Samsung()
obj.camera()

obj1=Nokia()
obj1.camera()
obj1.call()
