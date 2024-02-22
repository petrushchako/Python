class Peach:
    noOfPeachesCreated = 0

    def __init__(self,price, weight,origin) :
        self.price = price
        self.weight = weight
        self.origin = origin
        Peach.noOfPeachesCreated = Peach.noOfPeachesCreated + 1

    def removePeach (self) :
        Peach.noOfPeachesCreated = Peach.noOfPeachesCreated - 1


pl = Peach(2.50,2.15, 'Spain')
p2 = Peach(2.50,2.15, 'Spain')
p3 = Peach(2.50,2.15, 'Spain')
pl. removePeach()
print(Peach.noOfPeachesCreated)
p2. removePeach()
print(Peach.noOfPeachesCreated)
print(hasattr(p2, 'weight') )
print(hasattr(p2, 'noOfPeachesCreated'))