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

square_num = [num * num for num in numbers]
square_num2 = [(lambda x:x*x)(x) for x in numbers]

print("square_num: ",square_num)
print("square_num2: ",square_num2)

words_list = ["Hi", "there", "how", "are", "you"]
upper_words_list = [word.upper()[:2] for word in words_list]
print(f"{words_list} \n{upper_words_list}")
