# Simple example

numbers = [100, 200, 300, 400]

numbers_copy = []

for i in numbers:
    numbers_copy.append(i)

print(numbers_copy)

comprehension_copy = [num for num in numbers]
print(comprehension_copy)

# Enhanced comprehension example
numbers = [1,2,3,4,5,6]
odd_numbers = [num for num in numbers if (lambda x: x%2!=0)(num)]
even_numbers = [num for num in numbers if num%2==0]

print("Odd numbers (with lambda check): ", odd_numbers)
print("Even numbers:", even_numbers)