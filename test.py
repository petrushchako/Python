import copy
list1 = [1, [2, 3], 4]
list2 = copy.deepcopy(list1)
list3 = copy.copy(list1)
list3[1][1]='x'

print("List 1 : ",list1, "\nList 2 : ", list2, "\nList 3 : ", list3)


print("-"*30)

list_num = [20, 70, 80, 50, 30, 60, 40]

print(max(list_num))
print(min(list_num))
print(len(list_num))

list_num.sort() #Sort the origin list
print(sorted(list_num))

list_num.append(25)

print(list_num)

list_num_sorted = sorted(list_num, reverse=True)

print(list_num_sorted)

print(all([]))



print("-"*30)
cars= ["Audi", "BMW", "Mercedes-Benz", "Volkswagen", "Volvo"]
print(cars)
len(cars) # 4
cars[4] # Volvo
sliced_cars = cars[0:7] # ["Audi", "BMW", "Mercedes-Benz", "Volkswagen", "Volvo"]
print(sliced_cars)
sliced_cars = cars[0:-1:2] # ['Audi', 'Mercedes-Benz']
sliced_cars= cars[0::2] # ['Audi', 'Mercedes-Benz', 'Volvo']
reversed_cars=cars[6::-1]
print(reversed_cars)


my_car_list = ['Toyota Corolla', 'Toyota Camry', 'Nissan Altima', 'Kia Soul', 'Kia Optima', 'Honda Civic']
my_car_list[6:-1] = ['Ford Focus', 'Dodge Charger'] #Assign values to indexes 6 and 7/-1
print(my_car_list)
print(my_car_list[::-1])

print("Ford Focus" in my_car_list)
print(my_car_list.pop(-2))
print("Ford Focus" in my_car_list)


#### String as a list of characters
x = "World"
print(x[::2])

#x[0]="G"


x = "Hello"
print(x.startswith("H")) #True
print(x.startswith("h")) #False

print(x.endswith("o")) #True
print(x.endswith("O")) #False

print(x.count('l'))
print("-"*30)
print(x.count('l')) # 2
print(x.find("H")) # 0
print(x.find("h")) # -1
print(x.index("H"))
#print(x.index("h")) # ValueError: substring not found



x = "New York City"
y = []
z = ""

if(x.count(" ")> 0):
    y = x.split(" ")
    z = " ".join(y)
    print(y, "\n", z)


x1 = x[0:3]
print(x[1:3].islower())

print("-"*10, "TUPLES", "-"*10)
my_tuple = ()
print(my_tuple) # <class 'tuple'>

int_tuple = (1, 2, 3)
str_tuple = ("Hello", "Python")
print(int_tuple, str_tuple)

combinet_tuple = int_tuple + str_tuple
print(combinet_tuple * 2)

tuple1 = 1, "Hello", 3.14
print(tuple1) # <class 'tuple'>

a, b, c = tuple1
print(a, b, c)


print("Hello" in tuple1) #True
print(not("hello" not in tuple1))

x = (1, 2, 3, [4, 5])
x[3][1] = 100

print(x)

tuple_a = (1, 2, 3, 4, 5)
tuple_b = ( 'a', 'b', 'c' , 'd', 'e')

zipped = zip(tuple_a, tuple_b)
print(zipped) # ‹zip object at 0x10eb20b08>

result = tuple(zipped)
print(result)

t1, t2 = zip(*result)
print("t1: ", t1, "\nt2:", t2)


a =(" John", "Charles", "Mike")
b = ("Manager", "Supervisor", "Engineer")
x = zip(a, b)

c = dict(x)

print(c)


print("-"*50)

bike_owners = {
    "James":"Ducati Monster 1200", 
    "Jacob":"Ducati Scrambler 1100", 
    "William":"BMW S 1000 RR", 
    "Aiden":"Harley Davidson"
    }

print(bike_owners)
print(bike_owners.keys())
print(bike_owners.values())

for i in bike_owners:
    print(f" {i} : {bike_owners[i]}")
    
for i in bike_owners: print(i)

int_dict = {
    1 : "ONE",
    2 : "TWO",
    3 : "Three",
    3 : "THREE"
}

print("Aiden" in bike_owners)

bike_owners["Alex"] = "No bike"
bike_owners["Alex"] = "Lastochka"
print(bike_owners)



fruits = {
    'Banana': (50, 60, 40, 55),
    'Apple': (78, 86, 80, 60),
    'Apricot': [40, 70, 30, 55]}

print(fruits["Banana"][3])

for i in fruits:
    #print(i)
    for j in range(len(fruits[i])):
        print(fruits[i][j], end = ", ", sep = "-")
print("\n")
for i in fruits: 
    fruits["Apricot"][3] = 0.5
    
    for j in range(len(fruits[i])):
        print(fruits[i][j], end = ", ")

print("\n")

fruit_qty_consumed = {
    "Plum" : {'Fri': 70, 'Sat': 80},
    'Apple': {'Fri': 90, 'Sat': 95}
}

print(fruit_qty_consumed["Plum"]["Fri"])

print(fruit_qty_consumed.pop("Plum"))

print(fruit_qty_consumed.items())

for i,j in fruits.items():
    print(f"{i} : {j}")
    
    
fruits = {
    'Banana': (50, 60, 40, 55),
    'Apple': (78, 86, 80, 60),
    'Apricot': (40, 70, 30, 55),
    'Orange': (70, 80, 60, 65),
    'Avocado': (30, 50, 40, 45)}

# Remove item by key. Returns the value (i.e fruits.pop("Banana") -> (50, 60, 40, 55))
fruits.pop("Banana") 
fruits.popitem() # Removes random value from dict

# Sorting
sorted(fruits, reverse = True) # Returns the list of sorted keys
sorted(fruits.values()) # sort comparable values

# .items()
fruits.items() # Returns a list of tuples (key, value)
for i,j in fruits.items():
    print(f"{i} : {j}")

#Copy
copy_fruits = fruits.copy()



fruits = {
    'Banana': (50, 60, 40, 55),
    'Avocado': (30, 50, 40, 45)
    }

# Concatenate dicts
new_fruits = {"Cherry": (1, 2), "Banana": (1,2)}
fruits.update(new_fruits)
print(fruits)

print("-"*50)

set_string = {"Emma", "Olivia", "Ava", "Mia"}
print(set_string)

empty_set = set()
print(f"{empty_set} of type {type(empty_set)}")


a1 = {-1,0,1,2,3}
a2 = {1,2,3,4}

b1 = a1.intersection(a2)
print(b1)
b1 = a1.union(a2)
print(b1)
print(a1.difference(a2))
print(a2.symmetric_difference(a1))

a3 = {2,3}

print(a2.issuperset(a3))

set1 = {"Abc", "Bcd", "Cde"}

print(min(set1)) # Abc
print(max(set1)) # Cde


list1 = [[1,2],[3,4],[5,6]]
tuple1 = tuple(list1) # ([1,2],[3,4],[5,6])

print(tuple1)

set1 = set(tuple1)