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

