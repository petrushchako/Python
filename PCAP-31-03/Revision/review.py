##############################################
# Lambdas
##############################################

def add_func(a,b):
    return a+b

add_lambda = lambda a,b: a+b

assert add_func(2,3)== add_lambda(2,3)

print("Lambda example :" , add_lambda(2,3))





##############################################
# Collection functions
##############################################
domain = [1,2,3,4,5,6]

square_vals = list(map(lambda x: x**2, domain))
print("map() example:", square_vals)

evens = list(filter(lambda x: x%2==0, domain))
print("filter() example:", evens)

from functools import reduce
sum_of_values = reduce(lambda acc, num: acc+num, domain, 0)
print("Sum of numbers:", sum_of_values)

sentence = ["Boss", "a", "Alfred", "fig", "Daemon", "dig"]
print("\n\nSorting by default")
print(f"Original list:\n{sentence}")
print(f"sorted() default:\n{sorted(sentence)}")
print(f"sorted() with key:\n{sorted(sentence, key=lambda x: x.lower())}")

sentence.sort(key=str.lower, reverse=True)
print(f"Sorting with method and reverse:\n{sentence}")





##############################################
# Closures
##############################################

print("\n\nClosure examples:")

def message(msg):
    def name(name):
        return f"{msg} {name}"
    return name

closure_call = message("Hello")
print(closure_call('World'))


##############################################
# The 'if' operator
##############################################
print("\nif/if-else")

x = 1
y = 2

if x<y:
    print(f"y == {y}")
elif x>y:
    print(f"x == {x}")
else:
    print("Values are the same")


print(f"x == {x}" if x>y else f"y == {y}" if y>x else "Values are the same")

print(f"x == {x}") if x>y else print(f"y == {y}")



##############################################
# Creating and using modules
##############################################
from using_modules import helpers

print(''.join(helpers.extract_upper("New York")))




##############################################
# docstrings
##############################################

# Add docstrings and docstring test inside of the docstring.
# execute docstring with the following command:
# python -m doctest using_packages.heplers.strings.py --verbose


##############################################
# math and random
##############################################

# math(trigonometry): sin, cos, tan and hypot
# math(rounding): floor, ceil, trunc
# math(extras): sqrt, factorial, etc

# random
import random
print(random.randint(1,10)) # return 1-10 including


# choice()
# Define a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Choose a random fruit from the list
random_fruit = random.choice(fruits)
print("Random fruit chosen:", random_fruit)


# sample()
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Choose 3 unique random numbers from the list
random_numbers = random.sample(numbers, 3)
print("Random numbers chosen:", random_numbers)


# shuffle()
random.shuffle(numbers)
print("Shuffled numbers:", numbers)




##############################################
# platform
##############################################
import platform

print(platform.machine()) #x86_64
print(platform.platform()) #macOS-12.7.4-x86_64-i386-64bit
print(platform.processor()) #i386
print(platform.release()) #21.6.0
print(platform.python_version()) #3.12.1
print(platform.node()) #Oleksandrs-MBP.station
print(platform.uname()) #uname_result(system='Darwin', node='Oleksandrs-MBP.station', release='21.6.0', version='Darwin Kernel Version 21.6.0: Mon Feb 19 20:24:34 PST 2024; root:xnu-8020.240.18.707.4~1/RELEASE_X86_64', machine='x86_64')