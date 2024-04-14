from vehicle import Vehicle
from bicycle import Bicycle

civic = Vehicle('220_000',units="km")
print(civic.description())

bike = Bicycle()
print("\nBike instance:")
print(bike.description())