# Exception handling
try:
    num = int(input("Enter a number: "))
    r = 10 / num
    print(f"10 / {num} = {r}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero")
except ValueError:
    print("Error: Please enter a valid number")
except Exception as e:
    print("An error occured: " + e)
else:
    print("No exceptions occured")
finally:
    print("Execution completed")


def calculate_age(yob):
    current_year = 2025
    if yob > current_year:
        raise ValueError("Invalid birth year")
    return current_year - yob

try: 
    year_of_birth = int(input("Enter year of birth: "))
    print(f"Age: {calculate_age(year_of_birth)}")
except ValueError as ve:
    print(f"Error: {ve}")
    