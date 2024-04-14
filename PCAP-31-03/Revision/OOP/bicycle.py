from vehicle import Vehicle

class Bicycle(Vehicle):
    
    default_tire = "tire"

    def __init__(self, tires=None, milage = 0, units = "miles") -> None:
        super().__init__(milage, units)
        if not tires:
            tires = [self.default_tire, self.default_tire]
        self.tires = tires

    def description(self):
        initial =  super().description()
        return f"{initial} on {self.tires} tires"