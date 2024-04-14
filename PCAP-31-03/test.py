# Will generate [1,9]
numbers = [i*i for i in range (5) ]
foo = list(filter(lambda x: x % 2, numbers))
print(foo)



# Output: ++++++
def my_fun(n):
    s = "+"
    for i in range(n):
        s += s
        yield s
for x in my_fun(2):
    print(x, end='')



# This code will return function from class B, since it is the first one in the list of classes inherited
class A:
    def a(self):
        print('a')
class B:
    def a(self):
        print('b')
class C(B, A):
    def c(self):
        self.a()
o = C()
o.c()



# Sun Mon Tue Wed Thu Fri Sat
import calendar
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(3))



# 28 days, 22:00:00
from datetime import timedelta
delta = timedelta(weeks=1, days=7, hours=11)
print(delta*2)



# abc
class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
        def __iter__(self):
            return self      
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v
for x in I():
    print(x, end='')



# will print 2
x="\\\\"
print(len(x))
    


# __main__
print(__name__)



# TypeError: __init__() takes 1 positional argument but 2 were given
class A:
    def __init__(self):
        pass
a = A(1)
print(hasattr(a, 'A'))



# If `s` is a stream opened in read mode, the following
q = s.read(1) # One character from the stream




# 11:27:22
# When you subtract one datetime object from another in Python, you get a timedelta object representing the difference between the two datetime objects.

from datetime import datetime
datetime_1 = datetime(2019, 11, 27, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)
print(datetime_1 - datetime_2)



# False
class A:
    pass
class B(A):
    pass
class C(B):
    pass
print(issubclass(A,C)) # Class A is not a subclass of C, it is the other way around



# 3
class A:
    def __init__(self, v):
        self.v = v
    def set(self,v=1):
        self.v += v 
        return self.v
a = A()
b = a
b.set()
print(a.v)



# .pyc
# The compiled Python bytecode is stored in files which have their names ending with .pyc



# Will cause an error due to \"
x = "\\\"
print(len(x))



# r
print(chr(ord('p') + 2))



#1.3
print(float("1.3"))



# The code will raise an `AttributeError` exception
class A:
    def __init__(self, v):
        self.__a = v + 1
a = A(0)
print(a.__a)



# Base_Exception
try:
    raise Exception
except BaseException:
    print("Base_Exception")
except Exception:
    print("Exception")
except:
    print("except block")



# This code will read the file line by line
for x in open('file', 'rt'):
    print(x)




# 5 80 0
from random import *

a = random.randint(0,100)
b = random.randrange(10, 100, 3)
c = random.choice((0, 100, 3))


# pip uninstall command
# pip unisntall package_name



# False
class A:
    A = 1
    def __init__(self):
        self.a = 0

print(hasattr(A, 'a'))



# sys.stderr strem is normally associated with `the screen`



# The code will cause a syntax error
try:
    raise Exception
except:
    print('cdef')
except BaseException: # type: ignore
    print('abcd')
except Exception:     # type: ignore
    print('bcde')



# 3 
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))