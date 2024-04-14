class Vehicle:
    """
    Vehicle is the a class that represents the vecle(means of transportation)
    """

    def __init__(self, milage, units="miles") -> None:
        """
        Constructor for Vehicle class
        """
        self.milage = milage
        self.units = units

    # @classmethod
    # def bicycle(cls, tires=None):
    #     if not tires:
    #         tires = [cls.default_tire, cls.default_tire]
    #     return cls(None, tires)

    def description(self):
        return f"This {self.__class__.__name__} has travelled {self.milage} {self.units}"