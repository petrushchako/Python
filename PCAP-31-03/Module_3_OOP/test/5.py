class Vegetable:
    pass

class Potato (Vegetable) :
    pass

print(isinstance(Potato,Vegetable)) # Line 7
potato=Potato()
print(isinstance(potato, Potato)) # Line 9
print(isinstance(potato, Vegetable)) # Line 10
print(issubclass(potato, Potato)) # Line 12
print(issubclass(Potato, Vegetable))
# Line 13
print(issubclass(Vegetable, object)) # Line 14