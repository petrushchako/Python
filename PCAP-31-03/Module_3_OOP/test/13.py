class Banana:
    def __init__(self, weight,price, origin):
        self.weight = weight
        self.__price = price
        self.origin = origin

banana = Banana (5.0,1.85, "Spain")
print (banana. weight)
print (banana. price)
print (banana. origin)