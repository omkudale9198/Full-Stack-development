class Bank:
    __balance=0

    def setBalance(self,balance):
        self.__balance=balance

    def getBalance(self):
        return self.__balance

user=Bank()
user.setBalance(1000)
user.__balane=100000
print(user.getBalance())
