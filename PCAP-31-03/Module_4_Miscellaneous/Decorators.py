# Modifying code using Python Decorators

def non_negative_arguments(decorated_fn):
    def check_non_negative(*args):
        for arg in args:
            if arg <= 0:
                raise ValueError("Argument cannot be negative or zero")
        return decorated_fn(*args)
    return check_non_negative

@non_negative_arguments
def compute_rectangle_area(length, breadth):
    return length * breadth

print(compute_rectangle_area(3,4))
print(compute_rectangle_area(-3,4)) # Will raise ValueError from line 7


#Building decorator
#Step 1

def display_interesting_msg():
    print("Interesting message")

def display_borring_msg():
    print("Borring message")

def highlight_msg(func):
    print("*"*30)
    func()
    print("*"*30)

highlight_msg(display_borring_msg)
highlight_msg(display_interesting_msg)

# Output:
# ******************************
# Borring message
# ******************************
# ******************************
# Interesting message
# ******************************


# Step 2
# Introduce closures
def highlight(func):
    def highlight_msg():
        print("*"*30)
        func()
        print("*"*30)
    return highlight_msg
    
def display_interesting_msg():
    print("Interesting message")

def display_borring_msg():
    print("Borring message")
    
emphasize1=highlight(display_borring_msg) 
emphasize1()
emphasize2=highlight(display_interesting_msg) 
emphasize2()

# Step 3
# Instead of you initiating and calling clusre manually you can use @<closure outer function name> decorators to replace lines 61-62 and 63-64
def highlight(func):
    def highlight_msg():
        print("*"*30)
        func()
        print("*"*30)
    return highlight_msg

# When using @decorator, Python will create a closure installation call with the decorated function as input and then will execute the closure

@highlight
def display_interesting_msg():
    print("Interesting message")

@highlight
def display_borring_msg():
    print("Borring message")

display_interesting_msg()
display_borring_msg()



########################################################################################
# Input validation with decorators
import math

def check_numbers(fn):
    def check_for_negative(arg):
        if arg < 0:
            raise ValueError("Negative number provided")
        return fn(arg)
    return check_for_negative

@check_numbers
def compute_circle_area(radius):
    return math.pi * (radius**2)
