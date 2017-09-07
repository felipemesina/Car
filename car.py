
class Car(object):

    def __init__(self, price, speed, fuel, mileage):

        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.12
        if self.price>10000:
            self.tax = 0.15
        self.display_all()

    def display_all(self):
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "MPG: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + "mi"
        print "Tax: " + str(self.tax)
        print '\n'





car1 = Car(10000, 140, 30, 65000)

car2 = Car(8000, 140, 25, 95000)

car3 = Car(70000, 160, 22, 121)

car4 = Car(4000, 120, 30, 105000)

car5 = Car(2000, 120, 32, 165000)

car6 = Car(50000, 140, 25, 1000)
