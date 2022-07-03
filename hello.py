class Mobiles:
    def __init__(self,brand,mobile,price):
        self.brand=brand
        self.mobile=mobile
        self.price=price
    def disp(self):
        print("Brand:",self.brand)
        print("Mobile:",self.mobile)
        print("Price:",self.price)
        print("...................")

for i in range(5): 
    obj=Mobiles("Applesr","I10","20000")
    obj.disp()
