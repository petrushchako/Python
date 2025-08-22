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



