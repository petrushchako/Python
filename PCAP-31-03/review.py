##############################################
# Lambdas
##############################################

def add_func(a,b):
    return a+b

add_lambda = lambda a,b: a+b

assert add_func(2,3)== add_lambda(2,3)

print("Lambda example :" , add_lambda(2,3))
