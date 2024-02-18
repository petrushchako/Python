class Vegetable:
    def __init__(self, weight,price,origin):
        self.weight = weight
        self.price = price
        self.origin = origin

class Onion (Vegetable) :
    def __init__(self, weight,price, origin):
        super().__init__(weight,price, origin)


onion1=Onion (1.99,2.50, 'Ireland')
print(onion1.__name__)      #Line 15
print(Onion.__name__)       #Line 16
print(onion1.__module__)    #Line 17
print(Onion.__module__)     #Line 18
print(Onion.__bases__)      #Line 19
print(onion1.__bases__)     #Line 20