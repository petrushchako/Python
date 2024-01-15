
mixed_list = ["Nissan Sentra", 1, 2.5, True]

for i in mixed_list:
    print(type(i))

mixed_list[0] = "Ford Mondeo"
mixed_list.insert(7, "Audi")
mixed_list.insert(6, "BMW")

print(mixed_list)
