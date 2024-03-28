# Simple example

numbers = [100, 200, 300, 400]

numbers_copy = []

for i in numbers:
    numbers_copy.append(i)

print(numbers_copy)

comprehension_copy = [num for num in numbers]
print(comprehension_copy)