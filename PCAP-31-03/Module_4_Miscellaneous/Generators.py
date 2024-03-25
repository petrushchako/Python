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



print()

def fibonacci_gen():
    # Initial Fibonacci squence
    a,b = 0, 1 

    while True:
        yield a             #Return current Fibonacci number
        a, b = b, a + b     #Prep next Fibonacci number

fib_gen = fibonacci_gen()

for _ in range(30):
    print(next(fib_gen), end=" ")

print()