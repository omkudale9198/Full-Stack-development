cars={
    "Tata":{
        "Safari":{
            "Transmission:": "Manual and Automatic",
            "Milage: ":"16 kmpl",
            "Fuel type: ":"Diesel",
            "Price: ": "18 Lakh to 25 Lakh",
        },

        "Nexon":{
            "Transmission :": "Manual and Automatic",
            "Milage :":"21 kmpl",
            "Fuel type :":"Petrol & Diesel",
            "Price :": "8 Lakh to 11 Lakh",
        },

        "Nexon EV":{
            "Transmission :": "Automatic",
            "Milage :":"200 km in single charge",
            "Fuel type :":"Electric",
            "Price :": "10 Lakh to 15 Lakh",
        },
},
    "Suzuki":{
        "Ertiga":{
            "Transmission :": "Manual and Automatic",
            "Milage :":"25 kmpl",
            "Fuel type :":"CNG and Petrol",
            "Price :": "9.5 Lakh to 11 Lakh",
        },

        "Swift":{
            "Transmission :": "Manual and Automatic",
            "Milage :":"18 kmpl",
            "Fuel type :":"Petrol",
            "Price :": "6 Lakh to 8.5 Lakh",
        },

        "Baleno":{
            "Transmission :": "Manual and Automatic",
            "Milage :":"17 kmpl",
            "Fuel type :":"Petrol",
            "Price :": "7 Lakh to 10 Lakh",
        },
    },

    "Huyndai":{
        "Creta":{
            "Transmission :": "Manual and Automatic",
            "Milage :":"14 kmpl",
            "Fuel type :":"Petrol & Diesel",
            "Price :": "18 Lakh to 25 Lakh",
        },

        "i20":{
            "Transmission :": "Manual and Automatic",
            "Milage :":"18 kmpl",
            "Fuel type :":"Petrol",
            "Price :": "6.5 Lakh to 9 Lakh",
        },

        "Verna":{
            "Transmission :": "Manual and Automatic",
            "Milage :":"15 kmpl",
            "Fuel type :":"Petrol & Diesel",
            "Price :": "11 Lakh to 19 Lakh",
        }
    }
}
print("Welcome to Omkar's authorised showroom")

print("We have following brands:")
for i in cars:
    print(i, end=' ')

print()


class car:
    def brand(self,brand):
        self.brand=brand

        if(self.brand=="Tata" or self.brand=="Suzuki" or self.brand=="Huyndai"):
            print("----We have following models of",self.brand,"----")
            for i in cars[self.brand]:
                print(i)
        else:
            print("Brand name you have entered is wrong...")


       
        print("-----------------------------------")

    def model(self,model):
        self.model=model

        if (self.model in cars[self.brand]):
            print("--Details of", self.model,"--")
            for i,j in cars[self.brand][self.model].items():
                print(i,j)
        else:
            print("Model name you have entered is wrong...")

        print("-----------------------------------")



bname=1
while(bname!=0):
    brnd=input("Which brand's models would you like to see? ")
    obj=car()
    obj.brand(brnd)

    if brnd=="Tata" or brnd=="Suzuki" or brnd=="Huyndai":
        mdl=input("Which of the above model would you like to see in details? ")
        obj.model(mdl)

    bn=input("Would you like to see another model y/n? ")
    if(bn=="y"):
        bname=1
    else:
        bname=0
        print("Thanks for visiting...!")