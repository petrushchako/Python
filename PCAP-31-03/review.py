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






