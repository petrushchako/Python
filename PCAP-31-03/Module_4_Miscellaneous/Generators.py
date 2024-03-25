# Simple generator example

def myGenerator():
    print("First item")
    yield 10

    print("Second item")
    yield 20

    print("Third item")
    yield 30


gen = myGenerator()
next(gen)
print(gen, "\n")

count = 1
for i in myGenerator():
    print(i, " itearation number " ,count)
    count+=1

print("\nManually trigger generator:")
print(next(gen))
print("Some text in between")
print(next(gen))



print("\nFibonacci numbers:")

def fibonacci_gen():
    # Initial Fibonacci squence
    a,b = 0, 1 

    while True:
        yield a             #Return current Fibonacci number
        a, b = b, a + b     #Prep next Fibonacci number

fib_gen = fibonacci_gen()

for _ in range(30):
    print(next(fib_gen), end=" ")


# Use following syntax to prevent StopIterration exception
#fib_gen = fibonacci_gen()
#while True:
#    print(next(fib_gen, "Generator exhausted"))



print("\nCubes generator:")
def gen_cubes():
    for i in range(10):
        yield i ** 3

for i in gen_cubes():
    print(i, end=" ")


print("\nYou can also use tuple() to record all values in tuple format:\n" , tuple(gen_cubes()))
print(tuple(gen_cubes()))



# Interesting usage of yiled keyword example:
print("\nMessage receiver example:")
def message_receiver():
    while True:
        value = yield
        print(f"Received this message: {value}")

print(message_receiver)
receiver = message_receiver()
receiver.send(None)
receiver.send("Hello generator!")