def the_outer_function(x):
    language = x

    def inner_function():
        print(f"{x} is the best language")

    return inner_function

variable1 = the_outer_function("Python")
variable2 = the_outer_function("Java")
variable2()
variable1()





# Example 2
print()
def add_employee_to_department(department_name):
    employee_list = []

    def add_employee(employee_name):
        employee_list.append(employee_name)

        print(f"Added {employee_name} to {department_name}")
        print(f"{department_name} employees: {employee_list}\n")
    
    return add_employee

support = add_employee_to_department("Support")
dev = add_employee_to_department("Development")

support("Brian")
dev("John")
dev("Mike")


# Example 3
print()

def formal_greeting():
    greeting = "How are you doing?"

    def informal_greeting():
        nonlocal greeting #Will override variable from outer function
        greeting = "Hi there!"

        print(f"Greetingin the inner function: {greeting}")

    informal_greeting()
    print(f"Greeting in outer function: {greeting}")

formal_greeting()