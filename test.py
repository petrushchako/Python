import copy
list1 = [1, [2, 3], 4]
list2 = copy.deepcopy(list1)
list3 = copy.copy(list1)
list3[1][1]='x'

print("List 1 : ",list1, "\nList 2 : ", list2, "\nList 3 : ", list3)


print("\n"*3)

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