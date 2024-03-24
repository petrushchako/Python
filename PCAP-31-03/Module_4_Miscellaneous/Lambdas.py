# Simple lambda example
def increment_fn1(x):
    return x + 1

print(increment_fn1) # <function increment_fn at 0x109f4c900>

increment_fn2 = lambda x:x+1

print(increment_fn2) # <function <lambda> at 0x10c1b99d0>

# Invoke lambda function
print("Invoke Lambda function: increment_fn2(2) -> ", increment_fn2(2))


print("-"* 60,"\nRedefine functions functions lambda:\n")

# def square (number):
#     return number ** 2
square = lambda number: number ** 2

# def cube (number) :
#     return number ** 3
cube = lambda number: number ** 3

# def square_root (number):
#     return number ** (1/2)
square_root = lambda number: number ** 0.5

# def cube_root (number):
#     return number ** (1/3)
cube_root = lambda number: number ** (1/3)

# def raise_to_n (number, n):
#     return number ** n
raise_to_number = lambda number, n: number ** n

print("square : ", "\t"*3, square(3))
print("cube : ", "\t"*3, cube(2))
print("square_root : " ,"\t"*3, square_root(9))
print("cube_root : ", "\t"*3, cube_root(27))
print("raise_to_number : ", "\t"*2, raise_to_number(5,2))


create_list_fn = lambda item, times: [item for _ in range(times)]
print("create_list_fn(\"Huray!\", 3) : \t", create_list_fn("Huray!", 3))


print("(lambda x : x*10)(33) : \t",(lambda x : x*10)(33))
print("(lambda x,y: x*y)(33, 10) : \t",(lambda x,y: x*y)(33, 10))

print("-"* 60,"\n    \n")