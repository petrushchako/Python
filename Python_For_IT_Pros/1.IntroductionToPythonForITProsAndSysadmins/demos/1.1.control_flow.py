# if statement
age = 18
if age >= 18:
    print("You are now an adult :)")
print()


# if-else statement
temp = 25
if temp > 30:
    print("It is warm outside")
else:
    print("It is not too hot")
print()


# if-elif-else statement
res = 85
if res >= 90:
    grade = "A"
elif res >= 80:
    grade = "B"
elif res >= 70:
    grade = "C"
else:
    grade = "D"
# f-string
print(f"Your grade obtained is {grade}")
print()


# for-loop
fruits = ["apple", "banana", "grape"]
for fruit in fruits:
    print(f"Current fruit: {fruit}")
print()


# for loop with range()
for num in range(1, 6):
    print(f"Number: {num}")
print()


# while
cnt = 0
while cnt < 5:
    print(f"Count: {cnt}")
    cnt += 1
print()


# continue in for-loop
numbers = range(1, 7)
for num in numbers:
    if num % 2 == 0:
        print(f"Skipping this even number: {num}")
        continue
    print(f"Current number: {num}")
print()


# nested loops
for i in range(3):
    for j in range(3):
        print(f"i: {i} j: {j}")
print()


# recursion
def recursive(i, j):
    if i < 3:
        if j < 3:
            print(f"i: {i} j: {j}")
            recursive(i, j + 1)
        else:
            recursive(i + 1, 0)
    else:
        return


recursive(0, 0)
