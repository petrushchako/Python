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


letters = [x for x in "Harry Potter" if x.upper() in ['A', 'O', 'E', 'I', 'U']]
print(''.join(letters))


#########################################################################
import string

print("\n\nAlphabet examples")

lowercase_letters = list(string.ascii_lowercase)
print(lowercase_letters)
vowels = ['a','e','i','o','u']
consonant_letters = [x for x in lowercase_letters if x not in vowels]

print("\n\nConsonant Letters:")
for i, letter in enumerate(consonant_letters):
    if i % 5 == 0 and i != 0:
        print()
    print(letter, end=" ")


# Filter example    
filtered_alphabet = list(filter(lambda char: char not in vowels, lowercase_letters))
print("\n\nFiltered Alphabet:")

for i, letter in enumerate(filtered_alphabet):
    if i%5 == 0 and i != 0:
        print()
    print(letter, end = " ")


##############################################
print("\n"*2)
shapes = ["square", "circle", "triangle"]
colors = ["green", "white", "orange"]
combined = [(color,shape) for color in colors for shape in shapes]
print(combined)

print()
combined = [f"{color} {shape}" for shape, color in zip(shapes, colors)]
print(zip(colors, shapes))
print(combined)


#############################################
numbers =1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26
number_list = [x for x in range(200) if x%7 ==0 if x%13==0]
print(number_list)

num_tuples = [(i, "Even") if i%2==0 else (i, "Odd") for i in range(1,6)]
print(num_tuples)