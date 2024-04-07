# -3
import math
x = 1.7
print(-abs(math.floor(x) + math.ceil(x)))


# TRUE
# The directory from which the Python code is run is always searched through in order to find the necessary modules.
# Variables with names starting with two underscores are considered private inside their home module.
# FALSE
# The directory from which the code is run is never searched through.
# Variables with names ending with two underscores are considered private inside their home module.


# ('list index out of range',)
data = [261, 321]
try:
    print(data [-3])
except Exception as exception:
    print(exception. args)
else:
    print(" ('success',) ")



# -2
def attic(x):
    assert x != 0
    return 1/x
def floor(x):
    try:
        attic(x)
    except:
        raise
try:
    x = attic(0)
except RuntimeError:
    x = -3
except:
    x = -2
else:
    x = -1
print (x)



# e == 2
s = 'three'
e = 0
try:
    e = int(s)  # Value Error
except ArithmeticError:
    e = 1
except: 
    e = 2
else:
    e = 3
print(e)





# 0 
header = 2 *'+-' + '+' # +-+-+
plus = 0
for x in header: # The for loop iterates over each character in header. In this case, it iterates over each character in '+-+-+'.
    if not x in header: # Inside the loop, there is an if statement: if not x in header:. This condition checks if the current character x is not in the header. However, since x is always a character from header (due to the loop iterating over header itself), this condition will never be true.
        plus += 1
print (plus)




# TRUE
# Python accepts UTF-8 encoded source files.
# ASCII is a subset of UNICODE.
# FALSE
# In ASCII, Latin upper-case letter codepoints are greater than their lower-case counterparts.
# "/n" can be used to encode a new-line character.


# True False
class Cat:
    species = 1
    def get_species(self):
        return 'kitty'
    
class Tiger (Cat):
    def get_species(self):
        return 'tiggy'
    
def set_species(self):
    pass

creature = Tiger()
print(hasattr(creature, "Species"), hasattr(Cat, "set species"))





#Increment __b with fucntions:
# object._A__b += 1
# A._A__B += 1
class A:
    __b= 1
    def __init__(self):
        self.c = 1
def __action(self) :
    pass

object = A()





# TRUE
# isinstance(start, Button)
# selection.my_ID == 2
# FALSE
# selection is element
# start.my_ID ==-2
class Control:
    my_ID = 1
def say (self) :
    return self.my_ID
class Button(Control):
    my_ID = 2
class Radio(Button):
    def say(self):
        return -self. my_ID
selection = Radio()
element = Control()
start = Button()




#
class Diamond:
    pass
class Adamant(Diamond):
    pass
class Gem(Diamond):
    pass

# No exception:
class Jewel(Adamant, Diamond):
    pass
class Jewel(Adamant,Gem):
    pass
# Raise exception
class Jewel(Diamond, Diamond):
    pass
class Jewel(Diamond, Adamant):
    pass




# True no exception
#len(edition.__dict__ ! = len (Volume.__dict__)
# Volume.__dict__['chapter'] != None

# Fail or False
# 'paragraph' in Volume.__dict__
# paragraph' in edition.__dict__

class Volume:
    chapter = 1
    def __init__(self, paragraph):
        self.paragraph = paragraph
        Volume.chapter += 1
    def remove(self) :
        del self.paragraph
edition = Volume(1)
edition.remove()




# Soution below
class Un:
    value = "Ein"
    def say (self):
        return self.value.upper()
class Deux(Un):
    value = "Zwei"
class Troi(Un):
    def say(self):
        return self.value.lower()
class Quatre (Troi, Deux):
    pass
d = Quatre()
b = Deux()

#Solution
print(isinstance(d, Un)) # True
print(Troi in Quatre.__bases__) # True
# print(d.say("ZWEI")) # TypeError: say() takes 1 positional argument but 2 were given
print(d.say() == "ZWEI") # False
#print(q.value() =="uno") # NameError:name ' q'is not defined


#Valid Lambda
lambda a,b: a if a < b else b
lambda a,b: True
#Invalid lambda
# lambda a, b = a if a < b else b
# lambda (a, b) : return a if a < b else b


# The `errno.ENOENT`` symbol refers to an error described as:
# No such file or directory


# Prins 1 from array below
# [0, 1, 2, 4]
source = [1,2, 4, 8,16]
target = [x//2 for x in source if x < 10]
print(target[1])


# 1
pairs = [[2, 1], [-2, -1]]
new_pairs = map(lambda p: sorted(p) , pairs)
print(list(new_pairs)[0][0])



#TRUE
# There are three pre-opened file streams.
# The input() function reads data from the stdin stream.
# False
# The readlines() function returns a string.
# The first argument of the open() function is an integer value.





# Error will occure due to b(b)
def f(a, b):
    return b(b)
print(f(lambda x: x + 1, 0))




#True
def boolean(op):
    return op(False, True)
print(boolean(lambda x,y: x if x else y))




# 8 
def power(a):
    def internal(x):
        return x ** a;
    return internal
cube = power(3) # internal() with a==3
print(cube(2)) # 2 ** 3 == 8
