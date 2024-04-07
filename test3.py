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
header = 2 *'+-' + '+'
plus = 0
for x in header:
    if not x in header:
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