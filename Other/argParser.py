import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-a", "--first_operand", required=True, help="first operand")
ap.add_argument("-b", "--second_operand", required=True, help="second operand")

args = vars(ap.parse_args())

a = int(args["first_operand"])
b = int(args["second_operand"])

print(f"Sum is : {a+b}")
print(f"Sub is : {a-b}")
print(f"Div is : {a/b}")
print(f"Mul is : {a*b}")
