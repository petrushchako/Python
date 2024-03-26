def the_outer_function(x):
    language = x

    def inner_function():
        print(f"{x} is the best language")

    return inner_function

variable1 = the_outer_function("Python")
variable1()