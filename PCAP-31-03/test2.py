# 3
import math
x = -1.5
print(abs(math.floor(x) + math.ceil(x)))

# hypo() and sqrt() come from math

# __pycache__ 
#Contains semi-compiled module code
#It is created automatically

# import a.b
# a.b.c()
# you cannot invoke c() by c() or b.c()

# sys.path 
# It is a list of strings which indicates all directories/folders scanned by Python in order to find the specific modules.


#('3.14 is not in list')
consts = [3.141592, 2.718282]
try:
    print (consts.index(314e-2))
except Exception as exception:
    print (exception.args)
else:
    print ("success")




# -1
def fun (x):
    return 1/x
def mid_level(x):
    try:
        fun (x)
    except:
        raise AssertionError
    else:
        return 0
try:
    mid_level (0)
except Exception:
    x = -1
except:
    x = -2
print(x)




# launch , ignore

class Failure(IndexError):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "problem"
    
try:
    print('launch')
    raise Failure("ignition")
except RuntimeError as error:
    print(error)
except IndexError as error:
    print("igrnore")
else:
    print("landing")


# Follwoing methods may raise exceptions
# invoking int()
# indexing a list
    

# -1
x,y=3.0,0.0
try:
    z = x/y
except ArithmeticError:
    z = -1
except:
    z = -2
print(z)

# following two methods will return sorded letters string
letters = 'zyx'
tmp = list(letters)
tmp.sort()
new_string = ''.join(tmp)

new_string2 = ''.join(sorted(letters))


# Both expression evalue to True
chr(ord('k') + 2) == 'm'
ord('x') - ord('X') == ord(' ')

#following code will fail due to syntax error
plane = "Blackbird"
counter = 0
for i in plane + 2: # You cannot concatenate string with integer within loop 
    print(i)
    counter += 1
print(counter)


# Following expression return True
" " * 0 < 1 * " "
'Analog' < 'analog'
'' in 'abc'
#False
str(None) != 'None'
str(None) == None


#True
foo = "Mary had 21 little sheep"
print(foo.split()[2].isdigit())