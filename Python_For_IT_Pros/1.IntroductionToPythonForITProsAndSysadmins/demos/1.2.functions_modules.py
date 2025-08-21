# basic function
def hello(name):
    print(f"Hello {name}")
 
hello("stranger")


# return function
def add(a, b):
    return a + b

result = add(2,3)
print("Sum: ", result)


# function with named paramter
def power(base, exp=2):
    return base ** exp

print("2^3: ", power(2,3))
print("2^2: ", power(2))



def concatenate(*args):
    result = ""
    for arg in args:
        result += arg
    return result

print(concatenate("Python" , " ", "is", " ", "amazing"))